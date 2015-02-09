products_map = {'mmtt' : ('m1', 'm2', 't1', 't2', 'y'), 
                'eett' : ('e1', 'e2', 't1', 't2'),
                'mmmt' : ('m1', 'm2', 'm3', 't'),
                'eemt' : ('e1', 'e2', 'm', 't'),
                'mmet' : ('m1', 'm2', 'e', 't'),
                'eeet' : ('e1', 'e2', 'e', 't'),
                'mmem' : ('m1', 'm2', 'e', 'm3'),
                'eeem' : ('e1', 'e2', 'e3', 'm')
}

variables = ['LT_Higgs','Mass','mva_metEt','A_SVfitMass']
varZ = ['Mass', 'DR']
varH = ['Mass', 'SVfitMass', 'DR']
varAll = ['Pt']

channels = ['mmtt', 'eett', 'mmmt', 'eemt', 'mmet', 'eeet', 'mmem', 'eeem']

final = []
for channel in channels:
  for var in varZ:
    toAdd = products_map[channel][2] + '_' + products_map[channel][3] + '_' + var
    print "For channel: %s toAdd: %s" % (channel, toAdd)

print len(products_map['mmtt'])
