# -*- coding: utf-8 -*-
from Products.CMFPlone import interfaces as st_interfaces
from Products.CMFQuickInstallerTool import interfaces as qi_interfaces
from zope.interface import implements


PROJECTNAME = 'brasil.gov.portal'

LOCAL_TIME_FORMAT = '%d/%m/%Y'

TIME_FORMAT = '%Hh%M'

LOCAL_LONG_TIME_FORMAT = '{0} {1}'.format(LOCAL_TIME_FORMAT, TIME_FORMAT)

REDES = [
    {'id': 'facebook',
     'title': 'Facebook',
     'url': 'http://facebook.com/%s'},
    {'id': 'twitter',
     'title': 'Twitter',
     'url': 'https://twitter.com/%s'},
    {'id': 'youtube',
     'title': 'YouTube',
     'url': 'http://youtube.com/%s'},
    {'id': 'flickr',
     'title': 'Flickr',
     'url': 'http://flickr.com/%s'},
    {'id': 'googleplus',
     'title': 'Google+',
     'url': 'http://plus.google.com/%s'},
    {'id': 'slideshare',
     'title': 'Slideshare',
     'url': 'http://slideshare.com/%s'},
    {'id': 'soundcloud',
     'title': 'SoundCloud',
     'url': 'http://soundcloud.com/%s'},
    {'id': 'rss',
     'title': 'RSS',
     'url': '%s'},
    {'id': 'instagram',
     'title': 'Instagram',
     'url': 'http://instagram.com/%s'},
    {'id': 'tumblr',
     'title': 'Thumblr',
     'url': 'http://%s.tumblr.com'},
]

SHOW_DEPS = [
    'brasil.gov.agenda',
    'brasil.gov.barra',
    'brasil.gov.portlets',
    'brasil.gov.tiles',
    'brasil.gov.vcge',
    'collective.cover',
    'collective.nitf',
    'collective.polls',
    'sc.embedder',
    'sc.social.like',
]

DEPS = [
    'archetypes.querywidget',
    'brasil.gov.agenda.upgrades.v2000',
    'brasil.gov.agenda.upgrades.v3000',
    'brasil.gov.agenda.upgrades.v4000',
    'brasil.gov.portal.upgrades.v1000',
    'brasil.gov.portal.upgrades.v10300',
    'brasil.gov.portal.upgrades.v10400',
    'brasil.gov.portal.upgrades.v10500',
    'brasil.gov.portal.upgrades.v10600',
    'brasil.gov.portal.upgrades.v10700',
    'brasil.gov.portal.upgrades.v10800',
    'brasil.gov.portal.upgrades.v10802',
    'brasil.gov.portal.upgrades.v10803',
    'brasil.gov.portal.upgrades.v2000',
    'brasil.gov.portal.upgrades.v3000',
    'brasil.gov.portal.upgrades.v4000',
    'brasil.gov.portal.upgrades.v5000',
    'brasil.gov.portlets.upgrades.v1000',
    'brasil.gov.tiles.upgrades.v2000',
    'brasil.gov.vcge.at',
    'brasil.gov.vcge.dx',
    'brasil.gov.vcge.upgrades.v2000',
    'collective.googleanalytics',
    'collective.js.cycle2',
    'collective.js.galleria',
    'collective.js.jqueryui',
    'collective.portlet.calendar',
    'collective.upload',
    'collective.z3cform.datagridfield',
    'collective.z3cform.datetimewidget',
    'collective.z3cform.widgets',  # TODO: remove on release 2.0
    'ftw.upgrade',
    'plone.app.blocks',
    'plone.app.collection',
    'plone.app.contenttypes',
    'plone.app.dexterity',
    'plone.app.drafts',
    'plone.app.event',
    'plone.app.event.at',
    'plone.app.intid',
    'plone.app.iterate',
    'plone.app.jquery',
    'plone.app.jquerytools',
    'plone.app.querystring',
    'plone.app.relationfield',
    'plone.app.theming',
    'plone.app.tiles',
    'plone.app.versioningbehavior',
    'plone.formwidget.autocomplete',
    'plone.formwidget.contenttree',
    'plone.formwidget.datetime',
    'plone.formwidget.querystring',
    'plone.formwidget.recurrence',
    'plone.resource',
    'plone.session',
    'plonetheme.classic',
    'Products.Doormat',
    'Products.PloneFormGen',
    'raptus.autocompletewidget',
]

HIDDEN_PROFILES = [
    'archetypes.querywidget:default',
    'brasil.gov.agenda.upgrades.v2000:default',
    'brasil.gov.agenda.upgrades.v3000:default',
    'brasil.gov.agenda.upgrades.v4000:default',
    'brasil.gov.agenda:default',
    'brasil.gov.barra.upgrades.v1002:default',
    'brasil.gov.barra.upgrades.v1010:default',
    'brasil.gov.barra:default',
    'brasil.gov.portal.upgrades.v1000:default',
    'brasil.gov.portal.upgrades.v10300:default',
    'brasil.gov.portal.upgrades.v10300:default',
    'brasil.gov.portal.upgrades.v10400:default',
    'brasil.gov.portal.upgrades.v10500:default',
    'brasil.gov.portal.upgrades.v10600:default',
    'brasil.gov.portal.upgrades.v10700:default',
    'brasil.gov.portal.upgrades.v10800:default',
    'brasil.gov.portal.upgrades.v10802:default',
    'brasil.gov.portal.upgrades.v10803:default',
    'brasil.gov.portal.upgrades.v2000:default',
    'brasil.gov.portal.upgrades.v3000:default',
    'brasil.gov.portal.upgrades.v4000:default',
    'brasil.gov.portal.upgrades.v5000:default',
    'brasil.gov.portlets.upgrades.v1000',
    'brasil.gov.portal:default',
    'brasil.gov.portal:initcontent',
    'brasil.gov.portal:uninstall',
    'brasil.gov.tiles.upgrades.v2000:default',
    'brasil.gov.tiles:default',
    'brasil.gov.tiles:uninstall',
    'brasil.gov.vcge.at:default',
    'brasil.gov.vcge.dx:default',
    'brasil.gov.vcge.upgrades.v2000:default',
    'brasil.gov.vcge:default',
    'brasil.gov.vcge:uninstall',
    'collective.cover:default',
    'collective.js.cycle2:default',
    'collective.js.galleria:default',
    'collective.js.jqueryui:default',
    'collective.nitf:default',
    'collective.polls:default',
    'collective.portlet.calendar:default',
    'collective.portlet.calendar:uninstall',
    'collective.testcaselayer:testing',
    'collective.upload:default',
    'collective.z3cform.datagridfield:default',
    # TODO: remove collective.z3cform.widgets on release 2.0
    'collective.z3cform.widgets:1_to_2',
    'collective.z3cform.widgets:default',
    'collective.z3cform.widgets:test',
    'collective.z3cform.widgets:uninstall',
    'collective.z3cform.widgets:upgrade_1_to_2',
    'ftw.upgrade:default',
    'plone.app.blocks:default',
    'plone.app.caching:default',
    'plone.app.contenttypes:default',
    'plone.app.contenttypes:plone-content',
    'plone.app.dexterity:default',
    'plone.app.drafts:default',
    'plone.app.event.at:default',
    'plone.app.event:default',
    'plone.app.iterate:plone.app.iterate',
    'plone.app.jquerytools:default',
    'plone.app.openid:default',
    'plone.app.querystring:default',
    'plone.app.referenceablebehavior:default',
    'plone.app.relationfield:default',
    'plone.app.theming:default',
    'plone.app.tiles:default',
    'plone.app.versioningbehavior:default',
    'plone.formwidget.autocomplete:default',
    'plone.formwidget.contenttree:default',
    'plone.formwidget.querystring:default',
    'plone.formwidget.recurrence:default',
    'plone.session:default',
    'Products.CMFPlacefulWorkflow:base',
    'Products.Doormat:default',
    'Products.Doormat:uninstall',
    'Products.PloneFormGen:default',
    'Products.RedirectionTool:default',
    'raptus.autocompletewidget:default',
    'raptus.autocompletewidget:uninstall',
    'sc.embedder:default',
    'sc.microsite:default',
    'sc.social.like:default',
]

# http://www.tinymce.com/wiki.php/Configuration:formats
TINYMCE_JSON_FORMATS = {'strikethrough': {'inline': 'span',
                                          'classes': 'strikethrough',
                                          'exact': 'true'},
                        'underline': {'inline': 'span',
                                      'classes': 'underline',
                                      'exact': 'true'}}


class HiddenProducts(object):
    """ Oculta produtos do QuickInstaller """
    implements(qi_interfaces.INonInstallable)

    def getNonInstallableProducts(self):
        products = [p for p in DEPS]
        return products


class HiddenProfiles(object):
    """ Oculta profiles da tela inicial de criacao do site """
    implements(st_interfaces.INonInstallable)

    def getNonInstallableProfiles(self):
        return HIDDEN_PROFILES
