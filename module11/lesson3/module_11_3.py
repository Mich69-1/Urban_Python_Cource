# Домашнее задание по теме "Интроспекция"

from some_class import OhmLow
import inspect


def introspect_object(obj):
    obj_type = type(obj).__name__

    if hasattr(obj, '__dict__'):  # Проверка на наличие атрибута __dict__ (для пользовательских объектов)
        attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
        methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    else:
        attributes = []
        methods = [method for method in dir(obj)]

    parent_classes = [parent.__name__ for parent in getattr(obj, '__class__', type(obj)).__bases__]

    docstring = inspect.getdoc(obj)

    annotations = getattr(obj, '__annotations__', None)

    module = inspect.getmodule(obj).__name__ if inspect.ismodule(obj) else None

    file_path = None
    if inspect.ismodule(obj) or inspect.isclass(obj) or inspect.ismethod(obj) or inspect.isfunction(obj):
        file_path = inspect.getsourcefile(obj)

    introspection_result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'parent_classes': parent_classes,
        'docstring': docstring,
        'annotations': annotations,
        'module': module,
        'file_path': file_path
    }

    return introspection_result


# Пример использования
result_int = introspect_object(42)
result_str = introspect_object("Hello")
ooh = OhmLow(36, 100)
result_obj = introspect_object(ooh)
result_obj1 = introspect_object(ooh.get_current)
print(result_int)
print(result_str)
print(result_obj)
print(result_obj1)
