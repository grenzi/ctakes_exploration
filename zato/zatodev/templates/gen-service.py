from mako.template import Template
import re
import os

def service_verb_to_channelverb(name):
    return re.sub('(?<!^)(?=[A-Z])', '-', name).lower()

args = {}
args['noun'] = raw_input ('Enter noun (e.g., Corpus):')
args['verb'] = raw_input ('Enter verg (e.g., Create,Delete,Edit,GetById,GetList):')
args['channelmethods'] = ('GET', 'POST')
args['channelverb'] =service_verb_to_channelverb(args['verb'])
args['channelnoun'] =args['noun'].lower()


mytemplate = Template(filename='service.mako')
render =mytemplate.render(**args)

defaultfile='../services/{}/{}{}.py'.format(args['noun'], args['noun'], args['verb'])
res = raw_input('Save file as [{}]:'.format(defaultfile))
fileout = res or os.path.abspath(defaultfile)
print ('would save to {}'.format(fileout))

d = os.path.dirname(fileout)
if not os.path.exists(d):
    os.makedirs(d.lower())

text_file = open(fileout, "w")
text_file.write(render.replace('\r\n', '\n'))
text_file.close()

print 'Saved.'
