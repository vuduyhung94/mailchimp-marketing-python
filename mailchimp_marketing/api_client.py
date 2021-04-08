# coding: utf-8
"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.37
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import datetime
import requests
import json

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import quote

class ApiClientError(Exception):
    def __init__(self, text, status_code = None):
        self.text = text
        self.status_code = status_code

class ApiClient(object):
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types

    def __init__(self, config = {}):
        self.host = "https://server.api.mailchimp.com/3.0"
        self.default_headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Swagger-Codegen/3.0.37/python'
        }
        self.set_config(config)

    def get_server_from_api_key(self, api_key):
        try:
            split = api_key.split('-')
            server = 'invalid-server'

            if len(split) == 2:
                server = split[1]

            return server
        except:
            return ''


    def set_config(self, config = {}):
        # Basic Auth
        self.api_key = config['api_key'] if 'api_key' in config.keys() else ''
        self.is_basic_auth = self.api_key != ''

        # OAuth
        self.access_token = config['access_token'] if 'access_token' in config.keys() else ''
        self.is_oauth = self.access_token != ''

        # If using Basic auth and no server is provided,
        # attempt to extract it from the api_key directy.
        self.server = config['server'] if 'server' in config.keys() else 'invalid-server'
        if self.server == 'invalid-server' and self.is_basic_auth:
            self.server = self.get_server_from_api_key(self.api_key)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None, collection_formats=None, **kwargs):
        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v))
                )

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params, collection_formats)

        # request url
        url = self.host + resource_path

        if self.server:
            url = url.replace('server', self.server)

        # perform request and return response
        try:
            res = self.request(method, url, query_params, headers=header_params, body=body)
        except Exception as err:
            raise ApiClientError(err)

        try:
            if 'application/json' in res.headers.get('content-type'):
                data = res.json()
            else:
                data = res.text
        except Exception as err:
            data = None

        if data:
            if (res.ok):
                return data
            else:
                raise ApiClientError(text = data, status_code = res.status_code)
        else:
            return res

    def request(self, method, url, query_params=None, headers=None, body=None):
        auth = None

        if self.is_basic_auth:
            auth = ('user', self.api_key)

        if self.is_oauth:
            headers.update({ 'Authorization': 'Bearer ' + self.access_token })

        if method == "GET":
            return requests.get(url, params=query_params, headers=headers, auth=auth)
        elif method == "HEAD":
            return requests.head(url, params=query_params, headers=headers, auth=auth)
        elif method == "OPTIONS":
            return requests.options(url, params=query_params, headers=headers, auth=auth)
        elif method == "POST":
            return requests.post(url, data=json.dumps(body), params=query_params, headers=headers, auth=auth)
        elif method == "PUT":
            return requests.put(url, data=json.dumps(body), params=query_params, headers=headers, auth=auth)
        elif method == "PATCH":
            return requests.patch(url, data=json.dumps(body), params=query_params, headers=headers, auth=auth)
        elif method == "DELETE":
            return requests.delete(url, params=query_params, headers=headers, auth=auth)
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in six.iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: self.sanitize_for_serialization(val)
                for key, val in six.iteritems(obj_dict)}

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in six.iteritems(params) if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]
