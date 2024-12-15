from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime
from datetime import datetime, timezone
from database.connection import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    images = relationship("ProductImage", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")


class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    image_url = Column(String)  # Store URL or path to image

    product = relationship("Product", back_populates="images")
