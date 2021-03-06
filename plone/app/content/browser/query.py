# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from plone.app.querystring.interfaces import IQuerystringRegistryReader
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
import json


class QueryStringIndexOptions(BrowserView):

    def __call__(self):
        registry = getUtility(IRegistry)
        config = IQuerystringRegistryReader(registry)()
        self.request.response.setHeader("Content-Type", "application/json")
        return json.dumps(config)
