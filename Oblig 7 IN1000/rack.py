## Klasse for representasjon av racks i en regneklynge.
from node import Node
class Rack:

	def __init__(self):

	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
	def settInn(self, node):
		pass

	## Henter antall noder i racket
	# @return antall noder
	def getAntNoder(self):
		pass

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		pass

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		pass
