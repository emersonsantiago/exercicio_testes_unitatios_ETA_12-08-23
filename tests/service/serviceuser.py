import self as self

from tests.models.store import Store
from tests.models.user import User


class ServiceUser:
    def _init_(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.get_user_by_name(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "Usuário adicionado com sucesso"
                else:
                    return "Usuário já existe"
            else:
                return "Usuário não adicionado, pois não é uma string"
        else:
            return "Usuário não adicionado"



    def get_user_by_name(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None




    def remove_user(self, name):
        if name is not None:
            if isinstance(name, str):
                if self.get_user_by_name(name) is not None:
                    for user in self.store.bd:
                        if name == user.name:
                            self.store.bd.remove(user)
                        return "Usuário excluído com sucesso"
                else:
                    return "Usuário não encontrado"
            else:
                return "Usuário não é string"
        else:
            return "Usuário não foi excluído. Dados incompletos"




    def update_user(self, name, newJob):
        if name is not None and newJob is not None:
            if isinstance(name, str) and isinstance(newJob, str):
                user_to_update = self.get_user_by_name(name)
                if user_to_update is not None:
                    user_to_update.job = newJob
                    return "Usuário atualizado com sucesso"
                else:
                    return "Usuário não encontrado para atualização"
            else:
                return "Dados inválidos. Dados precisam ser string"
        else:
            return "Dados incompletos"