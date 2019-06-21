entity_url = 'http://180.179.214.221:9090/ngsi-ld/v1/entities/'
header={'content-type': 'application/ld+json', 'Accept-Charset': 'UTF-8'}
s_url='http://192.168.100.108:8080/ngsi10/subscribeContext'
jsonld_url="https://forge.etsi.org/gitlab/NGSI-LD/NGSI-LD/raw/master/coreContext/ngsi-ld-core-context.jsonld"
brand_url="http://example.org/"
id_value="urn:ngsi-ld:"
update_url='http://192.168.100.108:8080/ngsi10/updateContext'
create_status=201
update_status=204
internal_status=500
not_found_status=404
multistatus=207
fog_header={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

update_data= \
{
   "contextElements": [
    {
       "entityId": {
            "id": "Car31",
            "type": "Car",
            "isPattern": True
    },
       "attributes": [
            {
             "name": "brand40",
             "type": "string",
             "contextValue": "ford5"
            },
             {
             "name": "brand50",
             "type": "string",
             "contextValue": "ford6"
            }
     ],
       "domainMetadata": [
          {
           "name": "location",
           "type": "point",
           "value": {
              "latitude": 49.406393,
              "longitude": 8.684208
              }
           }
       ]
      }
    ],
 "updateAction": "UPDATE"
}

