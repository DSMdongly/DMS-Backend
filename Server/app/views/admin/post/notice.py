from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.admin.post.notice import *
from app.models.account import AdminModel
from app.models.post import NoticeModel


class NoticeManaging(Resource):
    @swag_from(NOTICE_MANAGING_POST)
    @jwt_required
    def post(self):
        """
        공지사항 업로드
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        title = request.form['title']
        content = request.form['content']

        NoticeModel(author=admin, title=title, content=content).save()

        return Response('', 201)

    @swag_from(NOTICE_MANAGING_PATCH)
    @jwt_required
    def patch(self):
        """
        공지사항 수정
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        id = request.form['id']
        title = request.form['title']
        content = request.form['content']

        notice = NoticeModel.objects(id=id).first()

        if not notice:
            return Response('', 204)

        notice.update(title=title, content=content)

        return Response('', 200)

    @swag_from(NOTICE_MANAGING_DELETE)
    @jwt_required
    def delete(self):
        """
        공지사항 제거
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            return Response('', 403)

        id = request.form['id']

        notice = NoticeModel.objects(id=id).first()

        if not notice:
            return Response('', 204)

        notice.delete()

        return Response('', 200)
