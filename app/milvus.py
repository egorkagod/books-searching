from fastapi import Request
from pymilvus import MilvusClient, DataType
from sentence_transformers import SentenceTransformer


def init_collection(client: MilvusClient, name="books") -> None:
    
        schema = client.create_schema(
            auto_id=True,
            enable_dynamic_field=True,
        )

        schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True)
        schema.add_field(field_name="vector", datatype=DataType.FLOAT_VECTOR, dim=1024)

        client.create_collection(
            collection_name=name,
            schema=schema
        )
        index_params = client.prepare_index_params()
        index_params.add_index(
            field_name="vector",
            index_type="HNSW",
            metric_type="COSINE",
            params={"M": 16, "efConstruction": 200},
        )
        client.create_index(name, index_params)
        client.load_collection(collection_name=name)


def get_milvus_client(req: Request) -> MilvusClient:
    return req.app.state.milvus


def get_embedder(req: Request) -> SentenceTransformer:
    return req.app.state.embedder
