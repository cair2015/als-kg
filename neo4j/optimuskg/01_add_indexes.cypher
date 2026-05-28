// Check duplicate or missing IDs first
MATCH (n)
UNWIND labels(n) AS label
WITH label, n
WHERE label IN ["GEN", "DIS", "DRG", "PHE", "ANA", "PWY", "BPO", "CCO", "MFN", "EXP"]
WITH label, n.id AS id, count(*) AS count
WHERE id IS NULL OR count > 1
RETURN label, id, count
ORDER BY label, count DESC;

// Create constraints
CREATE CONSTRAINT optimus_gen_id_unique IF NOT EXISTS FOR (n:GEN) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT optimus_dis_id_unique IF NOT EXISTS FOR (n:DIS) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT optimus_drg_id_unique IF NOT EXISTS FOR (n:DRG) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT optimus_phe_id_unique IF NOT EXISTS FOR (n:PHE) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT optimus_ana_id_unique IF NOT EXISTS FOR (n:ANA) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT optimus_pwy_id_unique IF NOT EXISTS FOR (n:PWY) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT optimus_bpo_id_unique IF NOT EXISTS FOR (n:BPO) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT optimus_cco_id_unique IF NOT EXISTS FOR (n:CCO) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT optimus_mfn_id_unique IF NOT EXISTS FOR (n:MFN) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT optimus_exp_id_unique IF NOT EXISTS FOR (n:EXP) REQUIRE n.id IS UNIQUE;

CREATE INDEX optimus_gen_symbol_index IF NOT EXISTS FOR (n:GEN) ON (n.symbol);
CREATE INDEX optimus_gen_name_index IF NOT EXISTS FOR (n:GEN) ON (n.name);
CREATE INDEX optimus_dis_name_index IF NOT EXISTS FOR (n:DIS) ON (n.name);
CREATE INDEX optimus_drg_name_index IF NOT EXISTS FOR (n:DRG) ON (n.name);

CREATE FULLTEXT INDEX optimus_node_text_fulltext IF NOT EXISTS
FOR (n:GEN|DIS|DRG|PHE|ANA|PWY|BPO|CCO|MFN|EXP)
ON EACH [n.id, n.name, n.symbol, n.description, n.synonyms, n.xrefs];

# Example query
CALL db.index.fulltext.queryNodes(
  "optimus_node_text_fulltext",
  "amyotrophic lateral sclerosis OR ALS"
)
YIELD node, score
RETURN labels(node) AS labels,
       node.id AS id,
       node.name AS name,
       node.symbol AS symbol,
       node.synonyms AS synonyms,
       score
ORDER BY score DESC
LIMIT 25;