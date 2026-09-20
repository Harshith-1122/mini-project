from sqlalchemy import text
from . import db


def execute_query(query, params=None):
    """Run any SQL statement and commit. Returns the result object."""
    try:
        result = db.session.execute(text(query), params or {})
        db.session.commit()
        return result
    except Exception:
        db.session.rollback()
        raise


def insert_record(query, params=None):
    """Run an INSERT statement and commit. Returns the new row ID (lastrowid)."""
    try:
        result = db.session.execute(text(query), params or {})
        db.session.commit()
        return result.lastrowid
    except Exception:
        db.session.rollback()
        raise


def update_record(query, params=None):
    """Run an UPDATE statement and commit. Returns the number of affected rows."""
    try:
        result = db.session.execute(text(query), params or {})
        db.session.commit()
        return result.rowcount
    except Exception:
        db.session.rollback()
        raise


def delete_record(query, params=None):
    """Run a DELETE statement and commit. Returns the number of affected rows."""
    try:
        result = db.session.execute(text(query), params or {})
        db.session.commit()
        return result.rowcount
    except Exception:
        db.session.rollback()
        raise


def fetch_records(query, params=None):
    """Run a SELECT statement. Returns a list of dictionary result rows."""
    try:
        result = db.session.execute(text(query), params or {})
        rows = [dict(row) for row in result.mappings()]
        return rows
    except Exception:
        db.session.rollback()
        raise
