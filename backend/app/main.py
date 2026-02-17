"""サンプル CRUD API"""

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Item
from app.schemas import ItemCreate, ItemResponse

app = FastAPI(
    title="Intern API",
    description="インターン事前課題：サンプル CRUD API",
    version="0.1.0",
)

# CORS設定（フロントエンド localhost:3000 からのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# ---------- Items CRUD （サンプル） ----------


@app.get("/items", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    """アイテム一覧を取得する"""
    return db.query(Item).all()


@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(body: ItemCreate, db: Session = Depends(get_db)):
    """アイテムを追加する"""
    item = Item(name=body.name)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """アイテムを削除する"""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
