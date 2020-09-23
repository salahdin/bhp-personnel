from edc_base.model_mixins import BaseUuidModel, ListModelMixin


class Studies(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'bhp_personnel'
