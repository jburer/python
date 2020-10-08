class Entitlement:
    name = "python"

    def change_name(self, new_name): # note that the first argument is self
        self.name = new_name # access the class attribute with the self keyword

    def entitlement_provisioning_def(self, entitlement, security_principal):
        pass

    def entitlement_deprovisioning_def(self, entitlement, security_principal):
        pass

    def permission_def(self, permission):
        pass

    def scope_def(self, scope):
        pass