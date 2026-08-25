from typing import Any, Optional


class List(list):
    

    __CRITERION_FUNCTION = {}

    def add_criterion(self, criterion_key: str, criterion_function) -> None:
       

        self.__CRITERION_FUNCTION[criterion_key] = criterion_function

    def show(self) -> None:
        
        # Muestra todos los elementos de la lista.
        

        for element in self:
            print(element)

    def search(
        self,
        search_value: Any,
        criterion: str = None
    ) -> Optional[int]:
        """
        Busca un elemento utilizando búsqueda binaria.

        La lista se ordena previamente según el criterio.

        Args:
            search_value: Valor que se desea encontrar.
            criterion (str): Criterio utilizado para buscar.

        Returns:
            int: Posición del elemento encontrado.
            None: Si el elemento no existe.
        """

        if not self:
            return None

        

        search_criterion = self.__CRITERION_FUNCTION.get(criterion)

        if search_criterion:
            if criterion in ("name", "real_name"):
                search_value = search_value.lower()


        self.sort_by_criterion(criterion)

        start = 0
        end = len(self) - 1

        while start <= end:

            middle = (start + end) // 2

            if search_criterion:
                value = search_criterion(self[middle])
            else:
                value = self[middle]

            if value == search_value:
                return middle

            elif value < search_value:
                start = middle + 1

            else:
                end = middle - 1

        return None

    def delete_value(
        self,
        value,
        criterion=None
    ) -> Optional[Any]:
        """
        Busca y elimina un elemento.

        Args:
            value: Valor que se desea eliminar.
            criterion: Criterio utilizado para buscar.

        Returns:
            El elemento eliminado o None si no existe.
        """

        index = self.search(value, criterion)

        if index is not None:
            return self.pop(index)

        return None

    def sort_by_criterion(self, key_criterion=None) -> None:
        """
        Ordena la lista utilizando un criterio.

        Args:
            key_criterion (str): Criterio utilizado para ordenar.
        """

        sort_criterion = self.__CRITERION_FUNCTION.get(key_criterion)

        if sort_criterion:
            self.sort(key=sort_criterion)

        elif self and isinstance(
            self[0],
            (bool, int, float, str)
        ):
            self.sort()

    def size(self) -> int:
        
        # Devuelve la cantidad de elementos de la lista.
        
        return len(self)

    def filter_contain_on_bio(self, values):
        """
        Muestra los personajes cuya biografía contiene
        alguna de las palabras indicadas.

        La búsqueda no distingue mayúsculas/minúsculas.

        Args:
            values (list): Palabras a buscar.
        """

        values = [value.lower() for value in values]

        for element in self:

            bio = element.bio.lower()

            if any(value in bio for value in values):
                print(element)

    def filter_start_with(self, values):
        """
        Muestra personajes cuyo nombre comienza con alguno
        de los prefijos indicados.

        Args:
            values (tuple): Prefijos a buscar.
        """

        for element in self:

            if element.name.startswith(values):
                print(element)

