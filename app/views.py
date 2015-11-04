# -*- coding: utf8 -*-
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.renderers import render_to_response
import pyramid.httpexceptions as exc
import sys, urllib, urllib2
import bs4 as bs


@view_config(route_name='home', renderer='app:templates/home.jinja2')
def home_page(request):
    if request.POST:                                                                                #""" Check if Submit button is pressed"""
        url                 = request.params['url']                                                 #""" Get the returned URL value """
        if not url or 'wiki' not in url:                                                            #""" Check if the ruturned URL value id NULL or if the word 'wekipedia' does not appear on the url string """
            raise exc.HTTPFound(request.route_url("home"))                                          #"""" Redirect back to the home page """
        else:                                                                                       #"""If the word 'wikipedia' appears on the url string, download the html using BeautifulSoup """
            data            = urllib.urlencode({'inputstring': ' '.join(sys.argv[1:])})
            info            = urllib2.urlopen(url, data)
            content         = info.read()
            soup            = bs.BeautifulSoup(content, "html.parser")  
            titleTag        = soup.html.head.title
            titleTag.string = 'Siyavula - Pyramid'
            h2Tag           = soup.new_tag("h2", style="font-size:20px; font-family:Arial, 'Arial Unicode MS', Helvetica, Sans-Serif; font-weight:normal; color: #B8A500;")
            h2Tag.string    = "Siyavula: "
            aTag            = soup.new_tag("a", href = "/")
            aTag.string     = "Home"
            h2Tag.insert(1, aTag)
            brTag           = soup.new_tag("br", style="color:black")
            soup.html.body.div.insert_after(brTag)
            soup.html.body.div.insert_before(h2Tag)
            soup.html.body.div
            f              = open('app/templates/wiki_page.jinja2', 'w')
            f.write('%s' % soup)
            f.close()

            raise exc.HTTPFound(request.route_url("new"))                                           #""" Redirect to the new page """
    return render_to_response('app:templates/home.jinja2', {'title': 'Siyavula'}, request=request)

@view_config(route_name='new', renderer='app:templates/wiki_page.jinja2')
def new_page(request):
    return render_to_response('app:templates/wiki_page.jinja2', {'title': 'Siyavula'}, request=request)
