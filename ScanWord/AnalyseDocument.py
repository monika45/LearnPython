from ScanWord.models.Catalog import Catalog
from ScanWord.models.Document import Document
from ScanWord.models.Item import Item
import docx


class AnalyseDocument:
    # 正文段落
    contentParas = []
    # 条款下标
    itemIndexes = []
    # 最小标题下标
    minCatalogIndexes = []

    # 最终数据。标题加条款
    data = []

    name = ''
    remark = ''

    # 目录大纲的字体
    outline_font = '楷体_GB2312'
    # 正文里的标题字体
    catalog_font = '黑体'
    # 正文里的条目的标题（正文条目内容必须用和所有标题不一样的字体）
    item_title_font = '黑体'

    def analyse(self, file):
        # 过滤空行后的段落，空行不参与解析
        filterdParas = [para for para in file.paragraphs if para.text != '']
        # 第一段是文档名
        self.name = filterdParas.pop(0).text
        # 第二段是备注
        self.remark = filterdParas.pop(0).text.replace('（', '').replace('）', '')
        # 过滤目录
        if filterdParas[0].text.startswith('目') and filterdParas[0].text.endswith('录'):
            filterdParas.pop(0)
        # 正文段落,  过滤目录大纲
        self.contentParas = [para for para in filterdParas if para.runs[0].font.name != self.outline_font]

        for paraIndex, para in enumerate(self.contentParas):
            if para.runs[0].text.startswith('第') and para.runs[0].text.endswith('条') and para.runs[0].font.name == self.item_title_font:
                self.itemIndexes.append(paraIndex)


    def complete_item(self, item_index):
        item = {
            'index': item_index,
            'title': self.contentParas[item_index].runs[0].text,
            'content':
        }
        current_para_cotent =

    def find_item_parent(self, item_index):
        """
        找条目的所属最小标题
        """
        index = item_index - 1
        while index >= 0:
            # 不是条目且不是条目内容（字体为标题字体）
            if index not in self.itemIndexes and self.contentParas[index].runs[0].font.name == self.catalog_font:
                break
            index = index - 1
        return index


    def find_catalog_parents(self, catalog_index):
        """
        返回上级的所有index列表，0->n,级别递减
        """
        parent_indexes = []
        index = catalog_index - 1
        while index >= 0:
            if index in self.itemIndexes or self.contentParas[index].runs[0].font.name != self.catalog_font:
                break
            parent_indexes.insert(0, index)
            index = index - 1
        return parent_indexes

    def catalog_title(self, catalog_index):
        return self.contentParas[catalog_index].text


if __name__ == '__main__':
    file = docx.Document('中华人民共和国民法典2020.docx')
    analyse = AnalyseDocument()
    analyse.analyse(file)


