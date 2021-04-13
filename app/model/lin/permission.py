from lin.model import Permission as LinPermission
from lin.model import db, manager


class Permission(LinPermission):
    @classmethod
    def select_by_group_id(cls, group_id) -> list:
        """
        get group permissions
        """
        query = db.session.query(manager.group_permission_model.permission_id).filter(
            manager.group_permission_model.group_id == group_id
        )
        result = cls.query.filter_by(soft=True, mount=True).filter(cls.id.in_(query))
        permissions = result.all()
        return permissions

    @classmethod
    def select_by_group_ids(cls, group_ids: list) -> list:
        """
        get group permissions
        """
        query = db.session.query(manager.group_permission_model.permission_id).filter(
            manager.group_permission_model.group_id.in_(group_ids)
        )
        result = cls.query.filter_by(soft=True, mount=True).filter(cls.id.in_(query))
        permissions = result.all()
        return permissions

    @classmethod
    def select_by_group_ids_and_module(cls, group_ids: list, module) -> list:
        """
        get group permissions by checking permission modules
        """
        query = db.session.query(manager.group_permission_model.permission_id).filter(
            manager.group_permission_model.group_id.in_(group_ids)
        )
        result = cls.query.filter_by(soft=True, module=module, mount=True).filter(
            cls.id.in_(query)
        )
        permissions = result.all()
        return permissions
