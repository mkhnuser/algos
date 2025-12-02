from typing import Hashable, Iterable, Mapping


class Graph:
    def __init__(
        self,
        *,
        vertices: Iterable[Hashable],
        edges: Iterable[Hashable],
        edges_to_vertices_mapping: Mapping,
    ) -> None:
        self.vertices = set(vertices)
        self.edges = set(edges)
        self.edges_to_vertices_mapping = edges_to_vertices_mapping


class UndirectedGraph(Graph):
    def __init__(
        self,
        *,
        vertices: Iterable[Hashable],
        edges: Iterable[Hashable],
        edges_to_vertices_mapping: Mapping,
    ) -> None:
        super().__init__(
            vertices=vertices,
            edges=edges,
            edges_to_vertices_mapping=edges_to_vertices_mapping,
        )


class DirectedGraph(Graph):
    def __init__(
        self,
        *,
        vertices: Iterable[Hashable],
        edges: Iterable[Hashable],
        edges_to_vertices_mapping: Mapping,
    ) -> None:
        super().__init__(
            vertices=vertices,
            edges=edges,
            edges_to_vertices_mapping=edges_to_vertices_mapping,
        )


if __name__ == "__main__":
    g = UndirectedGraph(
        vertices={"a", "b", "c"},
        edges={"e1", "e2", "e3"},
        edges_to_vertices_mapping={
            "e1": {"a", "b"},
            "e2": {"b", "c"},
            "e3": {"c", "a"},
        },
    )
