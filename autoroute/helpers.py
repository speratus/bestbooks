from autoroute.models import AutoroutingModel


class AutoroutingModelConverter:

    django_py_type_map = {
        'CharField': 'str',
        'BooleanField': 'bool',
        'BigAutoField': 'int',
        'CommaSeparatedIntegerField': 'str',
        'DecimalField': 'str',
        'AutoField': 'int',
        'BigIntegerField': 'int',
        'BinaryField': 'bytes',
        'DateField': 'date',
        'DateTimeField': 'datetime',
        'DurationField': 'timedelta',
        'EmailField': 'str',
        'FilePathField': 'str',
        'FloatField': 'float',
        'GenericIPAddressField': 'str',
        'IntegerField': 'int',
        'JSONField': 'str',
        'PositiveBigIntegerField': 'int',
        'PositiveIntegerField': 'int',
        'PositiveSmallIntegerField': 'int',
        'SlugField': 'str',
        'SmallAutoField': 'int',
        'SmallIntegerField': 'int',
        'TextField': 'str',
        'TimeField': 'time',
        'URLField': 'str',
        'UUIDField': 'str',
    }

    def __init__(self, model: AutoroutingModel):
        self.model = model

    @staticmethod
    def type_of_instance_attribute(model_instance, attribute: str):
        val = getattr(model_instance, attribute)
        return type(val).__name__

    @staticmethod
    def var_to_model_name(model):
        return type(model).__name__.lower()

    def type_of_model_attribute(self, model, attribute: str):
        raw_type = getattr(model, attribute).field.get_internal_type()
        key_exists = raw_type in self.django_py_type_map
        if not key_exists:
            raise KeyError(f"{attribute} attribute is not valid for use in a URL.")

        return self.django_py_type_map[raw_type]

    def urlconf_path_for_model_and_attribute(self, model: AutoroutingModel, attribute: str):
        prefix = self.var_to_model_name(model)
        att_type = self.type_of_model_attribute(model, attribute)
        return model.url_format % (prefix, att_type, attribute)


class ViewType:
    view_type = ''

    def __init__(self, model: AutoroutingModel, query_attributes: list, affected_attributes: list):
        self.model = model
        self.attributes = query_attributes
        self.affected_attributes = affected_attributes
        self.template_name = f'{self.view_name()}.html'

    @classmethod
    def reference_view_name(cls, model, *args):
        base = f'{AutoroutingModelConverter.var_to_model_name(model)}_{cls.view_type}'
        items = [base] + list(args)
        return '_'.join(items)

    def view_name(self):
        return self.reference_view_name(self.model, *self.attributes)

    def __str__(self):
        return self.view_name()

    def gen_view_function(self):
        raise NotImplemented("Method not implemented for base class")


class ReadView(ViewType):
    view_type = 'read'

    def gen_view_function(self):
        attributes = self.attributes
        affected = self.affected_attributes
        model = self.model
        model_name = AutoroutingModelConverter.var_to_model_name(model)
        template_name = self.template_name

        def view_fun(request, *args):

            criteria = {}
            for i in range(0, len(args)):
                criteria[attributes[i]] = args[i]

            item = model.objects.get(**criteria)

            response_data = {}
            for attribute in affected:
                response_data[attribute] = getattr(item, attribute)

            response_data[model_name] = item
            return render(request, template_name, response_data)

        view_fun.__name__ = self.view_name()
        return view_fun
