from mako.template import Template
import re

def service_verb_to_channelverb(name):
    return re.sub('(?<!^)(?=[A-Z])', '-', name).lower()



args = {}
args['noun'] = 'Corpus'
args['verb'] = 'Create'
args['channelmethods'] = ('GET', 'POST')
args['channelverb'] =service_verb_to_channelverb(args['verb'])
args['channelnoun'] =args['noun'].lower()


mytemplate = Template(filename='service.mako')

serviceverbtochannelverb = {'Create': 'create',
                            'Delete': 'delete',
                            'Edit':'edit',
                            'GetById':'get-by-id',
                            'GetList' : 'get-list'}


print(mytemplate.render(**args))
