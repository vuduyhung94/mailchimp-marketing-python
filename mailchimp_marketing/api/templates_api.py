# coding: utf-8

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.36
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_marketing.api_client import ApiClient


class TemplatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def delete_template(self, template_id, **kwargs):  # noqa: E501
        """Delete template  # noqa: E501

        Delete a specific template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The unique id for the template. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def delete_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Delete template  # noqa: E501

        Delete a specific template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The unique id for the template. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/templates/{template_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, **kwargs):  # noqa: E501
        """List templates  # noqa: E501

        Get a list of an account's available templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :param str created_by: The Mailchimp account user who created the template.
        :param str since_date_created: Restrict the response to templates created after the set date. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.
        :param str before_date_created: Restrict the response to templates created before the set date. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.
        :param str type: Limit results based on template type.
        :param str category: Limit results based on category.
        :param str folder_id: The unique folder id.
        :param str sort_field: Returns user templates sorted by the specified field.
        :param str sort_dir: Determines the order direction for sorted results.
        :return: Templates
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List templates  # noqa: E501

        Get a list of an account's available templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :param int count: The number of records to return. [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **10**. [Maximum value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **1000**
        :param int offset: The number of records from a collection to skip. Iterating over large collections with this parameter can be slow.  [Default value](/developer/guides/get-started-with-mailchimp-api-3/#Parameters) is **0**.
        :param str created_by: The Mailchimp account user who created the template.
        :param str since_date_created: Restrict the response to templates created after the set date. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.
        :param str before_date_created: Restrict the response to templates created before the set date. We recommend [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time format: 2015-10-21T15:41:36+00:00.
        :param str type: Limit results based on template type.
        :param str category: Limit results based on category.
        :param str folder_id: The unique folder id.
        :param str sort_field: Returns user templates sorted by the specified field.
        :param str sort_dir: Determines the order direction for sorted results.
        :return: Templates
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'exclude_fields', 'count', 'offset', 'created_by', 'since_date_created', 'before_date_created', 'type', 'category', 'folder_id', 'sort_field', 'sort_dir']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        if 'count' in params and params['count'] > 1000:  # noqa: E501
            raise ValueError("Invalid value for parameter `count` when calling ``, must be a value less than or equal to `1000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'created_by' in params:
            query_params.append(('created_by', params['created_by']))  # noqa: E501
        if 'since_date_created' in params:
            query_params.append(('since_date_created', params['since_date_created']))  # noqa: E501
        if 'before_date_created' in params:
            query_params.append(('before_date_created', params['before_date_created']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501
        if 'folder_id' in params:
            query_params.append(('folder_id', params['folder_id']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('sort_field', params['sort_field']))  # noqa: E501
        if 'sort_dir' in params:
            query_params.append(('sort_dir', params['sort_dir']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Templates',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_template(self, template_id, **kwargs):  # noqa: E501
        """Get template info  # noqa: E501

        Get information about a specific template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The unique id for the template. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: TemplateInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def get_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Get template info  # noqa: E501

        Get information about a specific template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The unique id for the template. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: TemplateInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/templates/{template_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemplateInstance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_default_content_for_template(self, template_id, **kwargs):  # noqa: E501
        """View default content  # noqa: E501

        Get the sections that you can edit in a template, including each section's default content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_default_content_for_template(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The unique id for the template. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: TemplateDefaultContent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_default_content_for_template_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_default_content_for_template_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def get_default_content_for_template_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """View default content  # noqa: E501

        Get the sections that you can edit in a template, including each section's default content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_default_content_for_template_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The unique id for the template. (required)
        :param list[str] fields: A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
        :param list[str] exclude_fields: A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
        :return: TemplateDefaultContent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id', 'fields', 'exclude_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_default_content_for_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'exclude_fields' in params:
            query_params.append(('exclude_fields', params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/templates/{template_id}/default-content', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemplateDefaultContent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_template(self, template_id, body, **kwargs):  # noqa: E501
        """Update template  # noqa: E501

        Update the name, HTML, or `folder_id` of an existing template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_template(template_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The unique id for the template. (required)
        :param TemplateInstance2 body:  (required)
        :return: TemplateInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_template_with_http_info(template_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_template_with_http_info(template_id, body, **kwargs)  # noqa: E501
            return data

    def update_template_with_http_info(self, template_id, body, **kwargs):  # noqa: E501
        """Update template  # noqa: E501

        Update the name, HTML, or `folder_id` of an existing template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_template_with_http_info(template_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: The unique id for the template. (required)
        :param TemplateInstance2 body:  (required)
        :return: TemplateInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling ``")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/templates/{template_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemplateInstance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create(self, body, **kwargs):  # noqa: E501
        """Add template  # noqa: E501

        Create a new template for the account. Only Classic templates are supported.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemplateInstance1 body:  (required)
        :return: TemplateInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add template  # noqa: E501

        Create a new template for the account. Only Classic templates are supported.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TemplateInstance1 body:  (required)
        :return: TemplateInstance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling ``")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/templates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemplateInstance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
