from algoliasearch_django import algolia_engine

def get_clint():
    return algolia_engine.client

def get_index(index_name='cfe_Product'):
    client = get_clint()
    index = client.init_index(index_name)
    return index



def perform_search(query, **kwargs):
    index = get_index()
    params = {}

    # Handle tags
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if tags:
            params['tagFilters'] = tags

    # Handle other filters
    index_filters = [f"{k}:{v}" for k, v in kwargs.items() if v]
    if index_filters:
        params['facetFilters'] = index_filters

    # IMPORTANT: pass params
    results = index.search(query, params)

    return results