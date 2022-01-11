from import_export import resources

from core.models.localization import Country, Governorates, City, Area


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country

class GovernoratesResource(resources.ModelResource):
    class Meta:
        model = Governorates
class CityResource(resources.ModelResource):
    class Meta:
        model = City
class AreaResource(resources.ModelResource):
    class Meta:
        model = Area