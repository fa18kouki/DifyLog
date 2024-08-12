# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from firebase_admin import credentials ,firestore
import datetime

cred = credentials.Certificate("./mykey.json")
initialize_app(cred)
db = firestore.client()
@https_fn.on_request(region='asia-northeast1')
def difyLogtest(req: https_fn.Request) -> https_fn.Response:
    try:
        user_id = req.args.get('user_id',00000000)

        # Firestoreにデータを追加
        doc_ref = db.collection(user_id).document()
        doc_ref.set({
            "user_id":user_id,
        })

        return https_fn.Response("データが正常に保存されました", status=200)

    except Exception as e:
        return https_fn.Response(f"エラーが発生しました: {str(e)}", status=500)
    
@https_fn.on_request(region='asia-northeast1')
def main(req: https_fn.Request) -> https_fn.Response:
    try:
        # URLパラメータから値を取得9noFkLGH3yG92Zow2sO9
        user_id = req.args.get('user_id',00000000000000000000)
        user_query = req.args.get('user_query',"不明")
        gender = req.args.get('gender',"不明")
        age = req.args.get('age',0)
        category = req.args.get('category',"その他")
        conversation_id = req.args.get('conversation_id',"不明")
        # カテゴリーを番号に変換
        category_mapping = {
            "StationAiの施設整備・運営に関する質問": 1,
            "StationAi全般に関する質問": 2,
            "オフィスに関する質問": 3,
            "支援プログラムに関する質問": 4,
            "起業サポートに関する質問": 5,
            "アクセスに関する質問": 6,
            "資料請求に関する質問": 7,
            "AI全般に関する質問": 8,
            "挨拶": 9,
            "その他": 10
        }
        category_number = category_mapping.get(category, 10)  # デフォルトは"その他"の10
        current_time = datetime.datetime.now()
        if gender == "男性":
            gender = 1
        elif gender == "女性":
            gender = -1
        else:
            gender = 0
        # Firestoreにデータを追加
        doc_ref = db.collection(user_id).document()
        doc_ref.set({
            "timestamp": current_time,
            "conversation_id":conversation_id,
            "user_query": user_query,
            "gender":gender,
            "age":age,
            "category":category_number
        })

        return https_fn.Response("データが正常に保存されました", status=200)

    except Exception as e:
        return https_fn.Response(f"エラーが発生しました: {str(e)}", status=500)