import ui
import Hensati as hs


class Basic:
	def __init__(self):
		self.items = []
		self.text__list = []
		
	def table_change(self):
		self.listdata = ui.ListDataSource("")
		self.listdata.items = self.items
		self.tableview = v['tableview1']
		self.tableview.data_source = self.listdata
		self.tableview.reload_data()
		
	def keisan(self):
		self.label = v['label2']
		self.textfield1 = v['textfield1']
		self.textfield2 = v['textfield2']
		self.textfield3 = v['textfield3']
		self.textfield4 = v['textfield4']
		self.textfield5 = v['textfield5']
		self.textfield6 = v['textfield6']
		self.textfield7 = v['textfield7']
		self.textfield8 = v['textfield8']
		self.textfield9 = v['textfield9']
		self.textfield10 = v['textfield10']
		self.i = hs.HensatiSansyutu()
		self.i.dosuu = [int(self.textfield3.text),int(self.textfield4.text),int(self.textfield5.text),int(self.textfield6.text),int(self.textfield7.text),int(self.textfield8.text),int(self.textfield9.text),int(self.textfield10.text)]
		self.kekka = self.i.Kekka(tensuu_mean=float(self.textfield1.text),syouei_tensuu=int(self.textfield2.text))
		self.label.text = self.kekka

b = Basic()
k = Basic()

def seg_change(sender):
	seg = v['segmentedcontrol1']
	if seg.selected_index == 0:
		b.items = [{"title": "225~250"}, {"title": "200~224"}, {"title": "175~199"}, {"title": "150~174"}, {"title": "125~149"}, {"title": "100~124"}, {"title": "75~99"}, {"title": "0~74"}]
		b.table_change()
		
	else:
		k.items = [{"title": "40~50"},{"title": "30~39"},{"title": "20~29"},{"title": "10~19"},{"title": "0~9"}]
		k.table_change()
		

def btn_sougou(sender):
	b.keisan()
	
def btn_kamoku(sender):
	label = v['label2']
	textfield1 = v['textfield1']
	textfield2 = v['textfield2']
	textfield3 = v['textfield3']
	textfield4 = v['textfield4']
	textfield5 = v['textfield5']
	textfield6 = v['textfield6']		
	textfield7 = v['textfield7']
	textfield8 = v['textfield8']
	textfield9 = v['textfield9']
	textfield10 = v['textfield10']
		
	i = hs.KamokubetuHS()
	i.dosuu = [int(textfield3.text),int(textfield4.text),int(textfield5.text),int(textfield6.text),int(textfield7.text)]
	kekka = i.Kekka(tensuu_mean=float(textfield1.text), syouei_tensuu=int(textfield2.text))
	label.text = kekka
v = ui.load_view()
v.present('sheet')


