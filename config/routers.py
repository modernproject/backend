from rest_framework import routers

class DefaultRouter(routers.DefaultRouter):

    def extend(self, router):
        self.registry.extend(router.registry)
