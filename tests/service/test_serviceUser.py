from tests.service.serviceuser import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        #Setup
        service = ServiceUser()
        expected_result = "Usuário adicionado com sucesso"

        #Chamada
        result = service.add_user("Emerson", "QA Analyst")

        #Validação
        assert result == expected_result



    def test_add_user_already_exists(self):
        #Setup
        service = ServiceUser()
        expected_result = "Usuário já existe"

        #Chamada
        result = service.add_user("Emerson", "QA Analyst")

        #Validação
        assert result == expected_result



    def test_search_user(self):
        #Setup
        service = ServiceUser()
        expected_result = "Emerson"

        #Chamada
        result = service.get_user_by_name(name="Emerson")

        #Validação
        assert result == expected_result



    def test_update_user(self):
        #Setup
        service = ServiceUser()
        expected_result = "Usuário atualizado com sucesso"

        #Chamada
        result = service.update_user("Emerson Santiago", "Analista de QA")

        #Validação
        assert result == expected_result



    def test_remove_user(self):
        #Setup
        service = ServiceUser()
        expected_result = "Usuário excluído com sucesso"

        #Chamada
        result = service.remove_user(name="Emerson Santiago")

        #Validação
        assert result == expected_result