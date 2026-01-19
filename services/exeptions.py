
class BusinessError(Exception):
    """Base para errores de lógica de negocio"""
    pass

class DatabaseConstraintError(BusinessError):
    """Específico para cuando fallan restricciones de integridad (FK)"""
    pass
