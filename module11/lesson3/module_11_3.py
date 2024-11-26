# Домашнее задание по теме "Интроспекция"

from some_class import OhmLow
import inspect


def introspect_inf(obj):
    '''Функция для интроспекции любого объекта'''

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

    # module = inspect.getmodule(obj).__name__   if inspect.ismodule(obj) else None

    file_path = None
    module = '__main__'
    if inspect.ismodule(obj) or inspect.isclass(obj) or inspect.ismethod(obj) or inspect.isfunction(obj):
        module = inspect.getmodule(obj).__name__
        file_path = inspect.getsourcefile(obj)

    introspection_result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'parent_classes': parent_classes,
        'docstring': docstring,
        'annotations': annotations,
        'file_path': file_path
    }

    return introspection_result


# Пример использования
result_int = introspect_inf(42)
result_str = introspect_inf("Hello")
ooh = OhmLow(36, 100)  # Пользовательский объект для примера
result_obj = introspect_inf(ooh)
result_obj1 = introspect_inf(ooh.get_current)
result_obj2 = introspect_inf(inspect)
result_obj3 = introspect_inf(introspect_inf)
print(result_int)
print(result_str)
print(result_obj)
print(result_obj1)
print(result_obj2)
print(result_obj3)
