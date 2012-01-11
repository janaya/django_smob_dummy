from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, redirect, render, \
    get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
#from django.contrib.auth.views import logout
from django.core import serializers
from django.conf import settings

import logging

def triples_person(request):
    person = """
<http://localhost:8000/data/person#me> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person>
<http://localhost:8000/data/person> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/PersonalProfileDocument>
<http://localhost:8000/data/person> <http://xmlns.com/foaf/0.1/maker> <http://localhost:8000/data/person#me>
<http://localhost:8000/data/person> <http://xmlns.com/foaf/0.1/primaryTopic> <http://localhost:8000/data/person#me>
<http://localhost:8000/data/person#me> <http://xmlns.com/foaf/0.1/nickname> "julia"

<http://localhost:8000/data/person#me> <http://xmlns.com/foaf/0.1/topic_interest> <http://dbpedia.org/resource/Semantic_Web>
<http://dbpedia.org/resource/Semantic_Web> <http://www.w3.org/2000/01/rdf-schema#label> "Semantic Web"
    """
    return HttpResponse(content=person,
#                        content_type='application/x-turtle')
                        content_type='text/turtle')

def rssrdf_post(request):
    rss = """<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns="http://purl.org/rss/1.0/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:cc="http://web.resource.org/cc/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:admin="http://webns.net/mvcb/" xmlns:atom="http://www.w3.org/2005/Atom"> 
 
<channel rdf:about="http://localhost:8000/"> 
  <title>SMOB Hub of </title> 
  <link>http://localhost:8000/</link> 
  <atom:link rel="hub" href="http://pubsubhubbub.appspot.com/subscribe"/> 
  <description>SMOB Hub of </description> 
  <dc:creator/> 
  <dc:date>2011-04-27T14:31:16+02:00</dc:date> 
  <admin:generatorAgent rdf:resource="http://smob.me/#smob?v=2.2"/> 
  <items> 
    <rdf:Seq>
      <rdf:li rdf:resource="http://localhost:8000/post/2011-04-27T14:26:46+02:00"/> 
    </rdf:Seq> 
  </items> 

</channel> 
  
<item rdf:about="http://localhost:8000/post/2011-04-27T14:26:46+02:00"> 
  <title>publisher110</title> 
  <link>http://localhost:8000/post/2011-04-27T13:45:31+02:00</link> 
  <description>publisher110</description> 
  <dc:creator>http://localhost:8000/data/person#me</dc:creator> 
  <dc:date>2011-04-27T13:45:31+02:00</dc:date> 
  <content:encoded>
    <![CDATA[<http://localhost:8000/> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smob.me/ns#Hub> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://rdfs.org/sioc/types#MicroblogPost> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://rdfs.org/sioc/ns#has_container> <http://localhost:8000/> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://rdfs.org/sioc/ns#has_creator> <http://localhost:8000/person> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://xmlns.com/foaf/0.1/maker> <http://localhost:8000/person#id> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://purl.org/dc/terms/created> "2011-04-27T13:45:31+02:00"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://purl.org/dc/terms/title> "Update - publisher110"^^<http://www.w3.org/2001/XMLSchema#string> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://rdfs.org/sioc/ns#content> "publisher110"^^<http://www.w3.org/2001/XMLSchema#string> .

    <http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#currentLocation> <http://sws.geonames.org/2964180/> .
    <http://sws.geonames.org/2964180/> <http://www.w3.org/2000/01/rdf-schema#label> "Galway city, Ireland (seat of a second-order administrative division)"^^<http://www.w3.org/2001/XMLSchema#string> .

    <http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://online-presence.net/opo/ns#OnlinePresence> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#declaredOn> <http://localhost:8000/person> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#declaredBy> <http://localhost:8000/person#me> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#StartTime> "2011-04-27T13:45:31+02:00"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
    <http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#customMessage> <http://localhost:8000/post/2011-04-27T13:45:31+02:00> .


    <http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://moat-project.org/ns#taggedWith> <http://dbpedia.org/resource/RDF> . 
    <http://localhost:8000/tagging/2011-04-27T13:45:31+02:00> <http://moat-project.org/ns#tagMeaning> <http://dbpedia.org/resource/RDF> .
    <http://localhost:8000/tagging/2011-04-27T13:45:31+02:00> <http://www.holygoat.co.uk/owl/redwood/0.1/tags/taggedResource> <http://localhost:8000/post/2011-04-27T13:45:31+02:00> .
    <http://localhost:8000/tagging/2011-04-27T13:45:31+02:00> <http://www.holygoat.co.uk/owl/redwood/0.1/tags/associatedTag> "RDF" .]]>
  </content:encoded> 
  <privacy><![CDATA[SELECT ?user WHERE { 
      ?user <http://purl.org/vocab/relationship/knows> <http://localhost:8000/data/person#me> . 
      ?user foaf:topic_interest <http://dbpedia.org/resource/Semantic_Web> .
    }]]>
  </privacy>
</item> 
</rdf:RDF>
    """
    return HttpResponse(content=rss,
                        content_type='application/rdf+xml') #application/rss+xml

def callback(request):
    
    if request.method == 'POST':
        logging.debug("method post")
        # get rss and store the external post update
    else: # GET
        logging.debug("method not post  ")
        # response with GET["hub_challenge"]

def add_post(request):
#    if request.is_ajax():
#        if form.is_valid():
#            response = {'status':True,}
#            json = simplejson.dumps(response, ensure_ascii=False)
#            return HttpResponse(json, mimetype="application/json")
#        else:
#            response = {'status':False,'errors':form.errors}
#            json = simplejson.dumps(response, ensure_ascii=False)
#            return HttpResponse(json, mimetype="application/json")
    triples = """
<http://localhost:8000/> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smob.me/ns#Hub> .

<http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://rdfs.org/sioc/types#MicroblogPost> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://rdfs.org/sioc/ns#has_container> <http://localhost:8000/> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://rdfs.org/sioc/ns#has_creator> <http://localhost:8000/person> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://xmlns.com/foaf/0.1/maker> <http://localhost:8000/person#id> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://purl.org/dc/terms/created> "2011-04-27T13:45:31+02:00"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://purl.org/dc/terms/title> "Update - 2011-04-27T13:45:31+02:00"^^<http://www.w3.org/2001/XMLSchema#string> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://rdfs.org/sioc/ns#content> "publisher110"^^<http://www.w3.org/2001/XMLSchema#string> .

<http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#currentLocation> <http://sws.geonames.org/2964180/> .
<http://sws.geonames.org/2964180/> <http://www.w3.org/2000/01/rdf-schema#label> "Galway city, Ireland (seat of a second-order administrative division)"^^<http://www.w3.org/2001/XMLSchema#string> .

<http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://online-presence.net/opo/ns#OnlinePresence> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#declaredOn> <http://localhost:8000/person> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#declaredBy> <http://localhost:8000/person#me> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#StartTime> "2011-04-27T13:45:31+02:00"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://localhost:8000/post/2011-04-27T13:45:31+02:00#presence> <http://online-presence.net/opo/ns#customMessage> <http://localhost:8000/post/2011-04-27T13:45:31+02:00> .


<http://localhost:8000/post/2011-04-27T13:45:31+02:00> <http://moat-project.org/ns#taggedWith> <http://dbpedia.org/resource/RDF> . 
<http://localhost:8000/tagging/2011-04-27T13:45:31+02:00> <http://moat-project.org/ns#tagMeaning> <http://dbpedia.org/resource/RDF> .
<http://localhost:8000/tagging/2011-04-27T13:45:31+02:00> <http://www.holygoat.co.uk/owl/redwood/0.1/tags/taggedResource> <http://localhost:8000/post/2011-04-27T13:45:31+02:00> .
<http://localhost:8000/tagging/2011-04-27T13:45:31+02:00> <http://www.holygoat.co.uk/owl/redwood/0.1/tags/associatedTag> "RDF" .
    """
    if request.method == 'POST':
        logging.debug("method post")
        #return redirect('home')
    else: # GET
        logging.debug("method not post  ")
    return render_to_response('djsmobdummy/post_add.html', 
                               {'triples': triples,
                               },
                               context_instance=RequestContext(request))


