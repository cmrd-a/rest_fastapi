from sqlalchemy import Column, Integer, String
import xml.etree.ElementTree as et
from .database import Base
from xml.dom import minidom


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)

    @property
    def xml(self):
        root = et.Element("Product")
        se_id = et.SubElement(root, "id")
        se_id.text = str(self.id)
        se_name = et.SubElement(root, "name")
        se_name.text = self.name
        se_price = et.SubElement(root, "price")
        se_price.text = str(self.price)
        reparsed = minidom.parseString(et.tostring(root, "utf-8"))
        return reparsed.toprettyxml()

