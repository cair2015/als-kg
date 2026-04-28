from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "2.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'alskb',
     'default_range': 'string',
     'description': 'Comprehensive ontology model for the ALS Knowledge Graph '
                    '(ALS-KG). Follows OWL 2 / RDF / OBO conventions with formal '
                    'class hierarchies, direct object properties, optional '
                    'evidence-bearing association classes, and semantic web '
                    'alignment. Suitable for export to OWL, RDF/Turtle, or '
                    'integration with biomedical ontology ecosystems.',
     'id': 'https://alskb.org/ontology/als_kg',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'als_kg',
     'prefixes': {'BFO': {'prefix_prefix': 'BFO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/BFO_'},
                  'CAS': {'prefix_prefix': 'CAS',
                          'prefix_reference': 'https://commonchemistry.cas.org/detail?cas_rn='},
                  'CTD': {'prefix_prefix': 'CTD',
                          'prefix_reference': 'http://ctdbase.org/detail.go?type=chem&acc='},
                  'ChEMBL': {'prefix_prefix': 'ChEMBL',
                             'prefix_reference': 'https://www.ebi.ac.uk/chembl/compound_report_card/'},
                  'ClinVar': {'prefix_prefix': 'ClinVar',
                              'prefix_reference': 'https://www.ncbi.nlm.nih.gov/clinvar/variation/'},
                  'DOI': {'prefix_prefix': 'DOI',
                          'prefix_reference': 'https://doi.org/'},
                  'DrugBank': {'prefix_prefix': 'DrugBank',
                               'prefix_reference': 'https://www.drugbank.ca/drugs/'},
                  'ECO': {'prefix_prefix': 'ECO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/ECO_'},
                  'ENSEMBL': {'prefix_prefix': 'ENSEMBL',
                              'prefix_reference': 'https://identifiers.org/ensembl/'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'HGNC': {'prefix_prefix': 'HGNC',
                           'prefix_reference': 'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'IAO': {'prefix_prefix': 'IAO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/IAO_'},
                  'ICD10CM': {'prefix_prefix': 'ICD10CM',
                              'prefix_reference': 'https://icd.codes/icd10cm/'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'MeSH': {'prefix_prefix': 'MeSH',
                           'prefix_reference': 'https://id.nlm.nih.gov/mesh/'},
                  'NCBIGene': {'prefix_prefix': 'NCBIGene',
                               'prefix_reference': 'https://www.ncbi.nlm.nih.gov/gene/'},
                  'OMIM': {'prefix_prefix': 'OMIM',
                           'prefix_reference': 'https://omim.org/entry/'},
                  'ORPHANET': {'prefix_prefix': 'ORPHANET',
                               'prefix_reference': 'http://www.orpha.net/ORDO/Orphanet_'},
                  'PMID': {'prefix_prefix': 'PMID',
                           'prefix_reference': 'https://pubmed.ncbi.nlm.nih.gov/'},
                  'RO': {'prefix_prefix': 'RO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/RO_'},
                  'SIO': {'prefix_prefix': 'SIO',
                          'prefix_reference': 'http://semanticscience.org/resource/'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'UMLS': {'prefix_prefix': 'UMLS',
                           'prefix_reference': 'https://uts.nlm.nih.gov/uts/umls/concept/'},
                  'UniProtKB': {'prefix_prefix': 'UniProtKB',
                                'prefix_reference': 'https://www.uniprot.org/uniprot/'},
                  'alskb': {'prefix_prefix': 'alskb',
                            'prefix_reference': 'https://alskb.org/ontology/'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'dbSNP': {'prefix_prefix': 'dbSNP',
                            'prefix_reference': 'https://www.ncbi.nlm.nih.gov/snp/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'obo': {'prefix_prefix': 'obo',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/'},
                  'oboInOwl': {'prefix_prefix': 'oboInOwl',
                               'prefix_reference': 'http://www.geneontology.org/formats/oboInOwl#'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'src/als_kg/schema/als_kg.yaml',
     'title': 'ALS Knowledge Graph Ontology Model',
     'types': {'ClinvarIdentifier': {'description': 'ClinVar variation numeric ID',
                                     'from_schema': 'https://alskb.org/ontology/als_kg',
                                     'name': 'ClinvarIdentifier',
                                     'pattern': '^\\d+$',
                                     'typeof': 'string',
                                     'uri': 'xsd:string'},
               'CtdIdentifier': {'description': 'CTD chemical/stressor identifier',
                                 'from_schema': 'https://alskb.org/ontology/als_kg',
                                 'name': 'CtdIdentifier',
                                 'typeof': 'string',
                                 'uri': 'xsd:string'},
               'DrugBankIdentifier': {'description': 'DrugBank primary identifier '
                                                     '(e.g. DB00533)',
                                      'from_schema': 'https://alskb.org/ontology/als_kg',
                                      'name': 'DrugBankIdentifier',
                                      'pattern': '^DB\\d{5}$',
                                      'typeof': 'string',
                                      'uri': 'xsd:string'},
               'GoIdentifier': {'description': 'Gene Ontology term identifier '
                                               '(e.g. GO:0006810)',
                                'from_schema': 'https://alskb.org/ontology/als_kg',
                                'name': 'GoIdentifier',
                                'pattern': '^GO:\\d{7}$',
                                'typeof': 'string',
                                'uri': 'xsd:string'},
               'HpoIdentifier': {'description': 'HPO phenotype term identifier '
                                                '(e.g. HP:0007354)',
                                 'from_schema': 'https://alskb.org/ontology/als_kg',
                                 'name': 'HpoIdentifier',
                                 'pattern': '^HP:\\d{7}$',
                                 'typeof': 'string',
                                 'uri': 'xsd:string'},
               'MondoIdentifier': {'description': 'MONDO disease ontology '
                                                  'identifier (e.g. MONDO:0007743)',
                                   'from_schema': 'https://alskb.org/ontology/als_kg',
                                   'name': 'MondoIdentifier',
                                   'pattern': '^MONDO:\\d{7}$',
                                   'typeof': 'string',
                                   'uri': 'xsd:string'},
               'NcbiGeneIdentifier': {'description': 'NCBI Entrez Gene numeric ID',
                                      'from_schema': 'https://alskb.org/ontology/als_kg',
                                      'name': 'NcbiGeneIdentifier',
                                      'pattern': '^\\d+$',
                                      'typeof': 'string',
                                      'uri': 'xsd:string'},
               'UberonIdentifier': {'description': 'UBERON anatomy ontology '
                                                   'identifier',
                                    'from_schema': 'https://alskb.org/ontology/als_kg',
                                    'name': 'UberonIdentifier',
                                    'pattern': '^UBERON:\\d+$',
                                    'typeof': 'string',
                                    'uri': 'xsd:string'},
               'UniprotIdentifier': {'description': 'UniProt accession identifier',
                                     'from_schema': 'https://alskb.org/ontology/als_kg',
                                     'name': 'UniprotIdentifier',
                                     'pattern': '^[A-Z0-9]{6}$',
                                     'typeof': 'string',
                                     'uri': 'xsd:string'}}} )

class DiseaseTypeEnum(str, Enum):
    sporadic = "sporadic"
    """
    Occurs without family history
    """
    familial = "familial"
    """
    Inherited pattern of occurrence
    """
    syndromic = "syndromic"
    """
    Part of larger syndrome
    """


class OnsetTypeEnum(str, Enum):
    bulbar = "bulbar"
    """
    Facial/tongue muscles affected first
    """
    limb = "limb"
    """
    Arm or leg muscles affected first
    """
    respiratory = "respiratory"
    """
    Breathing muscles affected first
    """
    generalized = "generalized"
    """
    Multiple sites affected simultaneously
    """
    unknown = "unknown"
    """
    Onset location unknown
    """


class GeneTypeEnum(str, Enum):
    protein_coding = "protein_coding"
    lncRNA = "lncRNA"
    miRNA = "miRNA"
    pseudogene = "pseudogene"
    other = "other"


class VariantTypeEnum(str, Enum):
    SNV = "SNV"
    """
    Single nucleotide variant
    """
    indel = "indel"
    """
    Insertion or deletion
    """
    repeat_expansion = "repeat_expansion"
    """
    Trinucleotide repeat expansion
    """
    CNV = "CNV"
    """
    Copy number variation
    """
    structural = "structural"
    """
    Structural variant (inversion, translocation)
    """


class RelationshipTypeEnum(str, Enum):
    """
    Standard relationship types following RDF/OWL semantics
    """
    is_a = "is_a"
    """
    Subclass relationship (taxonomic)
    """
    part_of = "part_of"
    """
    Mereological (compositional) relationship
    """
    proper_part_of = "proper_part_of"
    """
    Strict part-of (excludes identity)
    """
    participates_in = "participates_in"
    """
    Agent participates in process
    """
    has_participant = "has_participant"
    """
    Process has participant
    """
    regulates = "regulates"
    """
    Regulatory relationship (direction unspecified)
    """
    positively_regulates = "positively_regulates"
    """
    Upregulation/activation
    """
    negatively_regulates = "negatively_regulates"
    """
    Downregulation/inhibition
    """
    associated_with = "associated_with"
    """
    Statistical/empirical association
    """
    affects = "affects"
    """
    Causal or functional modification
    """


class EvidenceTypeEnum(str, Enum):
    curated = "curated"
    """
    Manually curated from literature
    """
    experimental = "experimental"
    """
    Derived from wet-lab experiments
    """
    computational = "computational"
    """
    Result of computational analysis
    """
    inferred = "inferred"
    """
    Inferred from other statements
    """
    predicted = "predicted"
    """
    Machine learning prediction
    """
    text_mined = "text_mined"
    """
    Extracted via natural language processing
    """



class NamedEntity(ConfiguredBaseModel):
    """
    Root class for all named entities in the ALS-KG ontology. Provides core ontology metadata (id, label, definition, synonyms, xrefs).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:NamedThing',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class OntologyClass(NamedEntity):
    """
    Abstract base for entity classes (nodes in knowledge graph). Inherits from NamedEntity with semantic web compatible metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'owl:Class',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class Relationship(ConfiguredBaseModel):
    """
    Abstract base for reified relationships (edges with explicit properties). Follows RDF triple pattern: subject, predicate, object. Can carry additional metadata (confidence, evidence, provenance).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'rdf:Statement',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    subject: str = Field(default=..., description="""Subject resource IRI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    predicate: str = Field(default=..., description="""Relationship type IRI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., description="""Object resource IRI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    confidence: Optional[str] = Field(default=None, description="""Confidence score (0-1)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of evidence supporting relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Citation or study ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    ingest_date: Optional[str] = Field(default=None, description="""Ingest date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })


class DiseaseOrPhenotype(OntologyClass):
    """
    Abstract parent class for all disease/phenotype entities. Following MONDO and HPO ontology patterns.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:DiseaseOrPhenotypicFeature',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    mondo_id: Optional[str] = Field(default=None, description="""MONDO cross-reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseOrPhenotype', 'Disease'], 'slot_uri': 'MONDO:'} })
    hpo_id: Optional[str] = Field(default=None, description="""HPO cross-reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseOrPhenotype', 'Phenotype'], 'slot_uri': 'HP:'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class Disease(DiseaseOrPhenotype):
    """
    Disease entity. Encompasses ALS (MONDO:0007743), related neurodegenerative disorders (FTD, PLS, PMA, SMA), and comorbidities. Follows MONDO disease hierarchy via is_a relationships.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Disease',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    mondo_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseOrPhenotype', 'Disease'], 'slot_uri': 'MONDO:'} })
    name: Optional[str] = Field(default=None, description="""Disease name (preferred from MONDO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'schema:name'} })
    disease_type: Optional[DiseaseTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'alskb:disease_type'} })
    onset_type: Optional[OnsetTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:onset_type'} })
    umls_cui: Optional[str] = Field(default=None, description="""UMLS Concept Unique Identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'UMLS:'} })
    omim_id: Optional[str] = Field(default=None, description="""OMIM (Online Mendelian Inheritance in Man) ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'OMIM:'} })
    orphanet_id: Optional[str] = Field(default=None, description="""Orphanet rare disease identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'ORPHANET:'} })
    icd10_code: Optional[str] = Field(default=None, description="""ICD-10-CM code for billing/clinical use""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'ICD10CM:'} })
    hpo_id: Optional[str] = Field(default=None, description="""HPO cross-reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseOrPhenotype', 'Phenotype'], 'slot_uri': 'HP:'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class Phenotype(DiseaseOrPhenotype):
    """
    Phenotypic feature (HPO term). Represents observable/measurable characteristics associated with diseases. Distinct from drug side effects which are modeled via DrugCausesPhenotype relationships.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:PhenotypicFeature',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    hpo_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseOrPhenotype', 'Phenotype'], 'slot_uri': 'HP:'} })
    frequency: Optional[str] = Field(default=None, description="""Frequency of phenotype in affected individuals (e.g. Frequent 75-99%)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:frequency'} })
    severity: Optional[str] = Field(default=None, description="""Severity scale""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:severity'} })
    mondo_id: Optional[str] = Field(default=None, description="""MONDO cross-reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseOrPhenotype', 'Disease'], 'slot_uri': 'MONDO:'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class Anatomy(OntologyClass):
    """
    Anatomical structure (UBERON ontology). ALS-specific relevance: motor cortex, spinal cord, anterior horn cells, neuromuscular junction. Linked to gene expression and disease manifestation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:AnatomicalEntity',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    uberon_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Anatomy'], 'slot_uri': 'UBERON:'} })
    bto_id: Optional[str] = Field(default=None, description="""Brenda Tissue Ontology ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Anatomy'], 'slot_uri': 'alskb:bto_id'} })
    mesh_id: Optional[str] = Field(default=None, description="""MeSH cross-reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['Anatomy', 'ExposureOrStressor'], 'slot_uri': 'MeSH:'} })
    anatomical_system: Optional[str] = Field(default=None, description="""Anatomical system classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['Anatomy'], 'slot_uri': 'alskb:anatomical_system'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class MolecularEntity(OntologyClass):
    """
    Abstract base for molecular-level entities (genes, proteins, variants). Directly related to disease mechanisms via molecular interactions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:MolecularEntity',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class Gene(MolecularEntity):
    """
    Human gene entity (Entrez/NCBI model). Separate from protein product to properly distinguish genotype from phenotype. Key ALS genes: C9orf72, SOD1, TARDBP, FUS, TBK1, NEK1, SQSTM1, VCP, OPTN.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Gene',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    ncbi_gene_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'NCBIGene:'} })
    hgnc_symbol: Optional[str] = Field(default=None, description="""Official HGNC gene symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein'], 'slot_uri': 'HGNC:'} })
    ensembl_id: Optional[str] = Field(default=None, description="""Ensembl gene identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'ENSEMBL:'} })
    chromosome: Optional[str] = Field(default=None, description="""Cytogenetic location (e.g. 21q22.11 for SOD1)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskb:chromosome'} })
    genomic_pos_start: Optional[int] = Field(default=None, description="""GRCh38 start coordinate (1-based)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskb:genomic_pos_start'} })
    genomic_pos_end: Optional[int] = Field(default=None, description="""GRCh38 end coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskb:genomic_pos_end'} })
    als_risk_tier: Optional[str] = Field(default=None, description="""Evidence tier for ALS association (ALSoD classification) - definitive, strong, moderate, or candidate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskb:als_risk_tier'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class TranscriptionFactor(Gene):
    """
    Gene encoding a transcription factor (TF). Subclass of Gene, carries both :Gene and :TranscriptionFactor labels. Source: DoRothEA + ENCODE TF annotations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:TranscriptionFactor',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    tf_family: Optional[str] = Field(default=None, description="""Structural family (C2H2-ZF, bHLH, Homeodomain, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactor'], 'slot_uri': 'alskb:tf_family'} })
    dorothea_confidence: Optional[str] = Field(default=None, description="""DoRothEA confidence level (A=high, D=low)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactor'], 'slot_uri': 'alskb:dorothea_confidence'} })
    ncbi_gene_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'NCBIGene:'} })
    hgnc_symbol: Optional[str] = Field(default=None, description="""Official HGNC gene symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein'], 'slot_uri': 'HGNC:'} })
    ensembl_id: Optional[str] = Field(default=None, description="""Ensembl gene identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'ENSEMBL:'} })
    chromosome: Optional[str] = Field(default=None, description="""Cytogenetic location (e.g. 21q22.11 for SOD1)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskb:chromosome'} })
    genomic_pos_start: Optional[int] = Field(default=None, description="""GRCh38 start coordinate (1-based)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskb:genomic_pos_start'} })
    genomic_pos_end: Optional[int] = Field(default=None, description="""GRCh38 end coordinate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskb:genomic_pos_end'} })
    als_risk_tier: Optional[str] = Field(default=None, description="""Evidence tier for ALS association (ALSoD classification) - definitive, strong, moderate, or candidate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskb:als_risk_tier'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class Protein(MolecularEntity):
    """
    Protein product (UniProt model). Distinct from Gene entity to capture protein-specific properties: aggregation propensity, prion-like domains, subcellular localization.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Protein',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    uniprot_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Protein'], 'slot_uri': 'UniProtKB:'} })
    protein_name: Optional[str] = Field(default=None, description="""Protein name (UniProt recommended name)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein'], 'slot_uri': 'schema:name'} })
    hgnc_symbol: Optional[str] = Field(default=None, description="""Gene name (cross-reference to Gene entity)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein'], 'slot_uri': 'HGNC:'} })
    molecular_weight_kda: Optional[float] = Field(default=None, description="""Molecular weight in kDa""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein'], 'slot_uri': 'alskb:molecular_weight_kda'} })
    protein_family: Optional[str] = Field(default=None, description="""Protein family classification (Pfam)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein'], 'slot_uri': 'alskb:protein_family'} })
    subcellular_location: Optional[list[str]] = Field(default=None, description="""Cellular compartment(s) where protein is localized (e.g. mitochondrion, nucleus, axon)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein'], 'slot_uri': 'alskb:subcellular_location'} })
    aggregation_prone: Optional[bool] = Field(default=None, description="""Known to form aggregates (TDP-43, SOD1, FUS)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein'], 'slot_uri': 'alskb:aggregation_prone'} })
    has_prion_like_domain: Optional[bool] = Field(default=None, description="""Contains intrinsically disordered prion-like region""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein'], 'slot_uri': 'alskb:has_prion_like_domain'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class Variant(MolecularEntity):
    """
    Genetic sequence variant (ClinVar model). Includes SNVs, indels, repeat expansions (C9orf72), and structural variants. Links to genes, proteins, and disease associations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:SequenceVariant',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    clinvar_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Variant'], 'slot_uri': 'ClinVar:'} })
    rsid: Optional[str] = Field(default=None, description="""dbSNP reference SNP ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variant'], 'slot_uri': 'dbSNP:'} })
    hgvs_c: Optional[str] = Field(default=None, description="""HGVS coding sequence notation (e.g. c.10A>G)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variant'], 'slot_uri': 'alskb:hgvs_c'} })
    hgvs_p: Optional[str] = Field(default=None, description="""HGVS protein notation (e.g. p.Ala4Val)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variant'], 'slot_uri': 'alskb:hgvs_p'} })
    variant_type: Optional[VariantTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant'], 'slot_uri': 'alskb:variant_type'} })
    clinical_significance: Optional[str] = Field(default=None, description="""ClinVar clinical interpretation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variant', 'VariantDiseaseAssociation'],
         'slot_uri': 'alskb:clinical_significance'} })
    als_class: Optional[str] = Field(default=None, description="""ALS-specific classification (causal, risk, modifier, protective)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variant'], 'slot_uri': 'alskb:als_class'} })
    maf: Optional[float] = Field(default=None, description="""Minor allele frequency in gnomAD non-neuro cohort""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['Variant'], 'slot_uri': 'alskb:minor_allele_frequency'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class ChemicalEntity(OntologyClass):
    """
    Abstract base for chemical and pharmacological entities (drugs, exposures, metabolites).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:ChemicalEntity',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class Drug(ChemicalEntity):
    """
    Pharmaceutical compound (DrugBank model). ALS-approved drugs: Riluzole, Edaravone, Tofersen, AMX0035. Includes mechanism, targets, side effects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Drug',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    drugbank_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Drug'], 'slot_uri': 'DrugBank:'} })
    drug_name: Optional[str] = Field(default=None, description="""Preferred drug name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug'], 'slot_uri': 'schema:name'} })
    chembl_id: Optional[str] = Field(default=None, description="""ChEMBL compound ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug'], 'slot_uri': 'ChEMBL:'} })
    inchi_key: Optional[str] = Field(default=None, description="""Standard InChIKey hash""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug'], 'slot_uri': 'alskb:inchi_key'} })
    smiles: Optional[str] = Field(default=None, description="""Canonical SMILES string""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug'], 'slot_uri': 'alskb:smiles'} })
    drug_type: Optional[str] = Field(default=None, description="""Categorization (small molecule, biologic, ASO, cell therapy, gene therapy)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug'], 'slot_uri': 'alskb:drug_type'} })
    als_approved: Optional[bool] = Field(default=None, description="""FDA approval status for ALS treatment""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug'], 'slot_uri': 'alskb:als_approved'} })
    trial_status: Optional[str] = Field(default=None, description="""Highest clinical trial phase reached""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug'], 'slot_uri': 'alskb:trial_status'} })
    mechanism: Optional[str] = Field(default=None, description="""Known mechanism of action""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugTargetAssociation', 'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:mechanism'} })
    indication: Optional[str] = Field(default=None, description="""Clinical indication""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug'], 'slot_uri': 'alskb:indication'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class ExposureOrStressor(ChemicalEntity):
    """
    Environmental exposure or chemical stressor from CTD ontology. ALS-relevant: BMAA, organophosphate pesticides, heavy metals, solvents.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:ChemicalSubstance',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    ctd_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureOrStressor'], 'slot_uri': 'CTD:'} })
    exposure_name: Optional[str] = Field(default=None, description="""Standard name of exposure/stressor""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureOrStressor'], 'slot_uri': 'schema:name'} })
    exposure_type: Optional[str] = Field(default=None, description="""Category (chemical, metal, pesticide, radiation, biological, other)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureOrStressor'], 'slot_uri': 'alskb:exposure_type'} })
    mesh_id: Optional[str] = Field(default=None, description="""MeSH ID for exposure agent""", json_schema_extra = { "linkml_meta": {'domain_of': ['Anatomy', 'ExposureOrStressor'], 'slot_uri': 'MeSH:'} })
    cas_number: Optional[str] = Field(default=None, description="""CAS Registry number""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureOrStressor'], 'slot_uri': 'CAS:'} })
    als_relevance: Optional[bool] = Field(default=None, description="""Flagged as ALS-relevant in literature""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureOrStressor'], 'slot_uri': 'alskb:als_relevance'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class BiologicalConcept(OntologyClass):
    """
    Abstract base for functional/biological concepts from GO and related ontologies. Represents processes, functions, and compartments involved in ALS pathology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'alskb:BiologicalConcept',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class BiologicalProcess(BiologicalConcept):
    """
    Gene Ontology Biological Process term. ALS-relevant: protein aggregation, oxidative stress, neuroinflammation, axonal transport, neurodegeneration, apoptosis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:BiologicalProcess',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    go_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalProcess', 'MolecularFunction', 'CellularComponent'],
         'slot_uri': 'GO:'} })
    process_name: Optional[str] = Field(default=None, description="""Standard process name from GO""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalProcess'], 'slot_uri': 'schema:name'} })
    go_definition: Optional[str] = Field(default=None, description="""GO textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalProcess', 'MolecularFunction', 'CellularComponent'],
         'slot_uri': 'IAO:0000115'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class MolecularFunction(BiologicalConcept):
    """
    Gene Ontology Molecular Function term. Describes biochemical activities (catalytic, binding, etc.) performed by gene products.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:MolecularActivity',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    go_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalProcess', 'MolecularFunction', 'CellularComponent'],
         'slot_uri': 'GO:'} })
    function_name: Optional[str] = Field(default=None, description="""Molecular function name from GO""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularFunction'], 'slot_uri': 'schema:name'} })
    go_definition: Optional[str] = Field(default=None, description="""GO textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalProcess', 'MolecularFunction', 'CellularComponent'],
         'slot_uri': 'IAO:0000115'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class CellularComponent(BiologicalConcept):
    """
    Gene Ontology Cellular Component term. ALS-critical compartments: stress granule, P-body, cytoplasm, nucleus, axon, neuromuscular junction, mitochondrion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:CellularComponent',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    go_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalProcess', 'MolecularFunction', 'CellularComponent'],
         'slot_uri': 'GO:'} })
    component_name: Optional[str] = Field(default=None, description="""Cellular component name from GO""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellularComponent'], 'slot_uri': 'schema:name'} })
    go_definition: Optional[str] = Field(default=None, description="""GO textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalProcess', 'MolecularFunction', 'CellularComponent'],
         'slot_uri': 'IAO:0000115'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class DiseaseSubtype(Disease):
    """
    Molecularly-defined disease subtype derived from clustering analysis (transcriptomics, proteomics, multi-omics). Represents cohort stratification. Links to Disease via is_a relationship; carries distinct clinical correlates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:DiseaseSubtype',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    subtype_id: Optional[str] = Field(default=None, description="""Custom subtype identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype'], 'slot_uri': 'alskb:subtype_id'} })
    cluster_method: Optional[str] = Field(default=None, description="""Clustering approach (NMF, WGCNA, scRNA-seq, consensus)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype'], 'slot_uri': 'alskb:cluster_method'} })
    cluster_id: Optional[int] = Field(default=None, description="""Cluster number from analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype'], 'slot_uri': 'alskb:cluster_id'} })
    signature_genes: Optional[list[str]] = Field(default=None, description="""Top discriminative genes for subtype""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype'], 'slot_uri': 'alskb:signature_genes'} })
    n_patients: Optional[int] = Field(default=None, description="""Number of patients in subtype""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype'], 'slot_uri': 'alskb:n_patients'} })
    cohort: Optional[str] = Field(default=None, description="""Source patient cohort (AnswerALS, NYGC, PRO-ACT)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype', 'DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:cohort'} })
    clinical_correlate: Optional[str] = Field(default=None, description="""Associated clinical feature or phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype'], 'slot_uri': 'alskb:clinical_correlate'} })
    median_survival_months: Optional[float] = Field(default=None, description="""Median survival from symptom onset""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype'], 'slot_uri': 'alskb:median_survival_months'} })
    source_publication: Optional[str] = Field(default=None, description="""DOI or PMID reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype'], 'slot_uri': 'dcterms:bibliographicCitation'} })
    mondo_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseOrPhenotype', 'Disease'], 'slot_uri': 'MONDO:'} })
    name: Optional[str] = Field(default=None, description="""Disease name (preferred from MONDO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'schema:name'} })
    disease_type: Optional[DiseaseTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'alskb:disease_type'} })
    onset_type: Optional[OnsetTypeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:onset_type'} })
    umls_cui: Optional[str] = Field(default=None, description="""UMLS Concept Unique Identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'UMLS:'} })
    omim_id: Optional[str] = Field(default=None, description="""OMIM (Online Mendelian Inheritance in Man) ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'OMIM:'} })
    orphanet_id: Optional[str] = Field(default=None, description="""Orphanet rare disease identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'ORPHANET:'} })
    icd10_code: Optional[str] = Field(default=None, description="""ICD-10-CM code for billing/clinical use""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'ICD10CM:'} })
    hpo_id: Optional[str] = Field(default=None, description="""HPO cross-reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseOrPhenotype', 'Phenotype'], 'slot_uri': 'HP:'} })
    source_version: Optional[str] = Field(default=None, description="""Source database/ontology version""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    ingest_date: Optional[str] = Field(default=None, description="""When entity was imported into ALS-KG""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    id: str = Field(default=..., description="""Persistent unique identifier (IRI)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Preferred human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'IAO:0000115'} })
    synonym: Optional[str] = Field(default=None, description="""Alternative names""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasRelatedSynonym'} })
    xref: Optional[str] = Field(default=None, description="""Cross-references to external ontologies""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'oboInOwl:hasDbXref'} })
    comment: Optional[str] = Field(default=None, description="""Informal notes or comments""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:comment'} })
    is_obsolete: Optional[str] = Field(default="false", description="""Deprecation flag""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'ifabsent': 'false',
         'slot_uri': 'owl:deprecated'} })
    source: Optional[str] = Field(default=None, description="""Original source/database""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    last_updated: Optional[str] = Field(default=None, description="""Last modification timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class Association(Relationship):
    """
    Abstract base for optional evidence-bearing associations. Use when a relationship cannot be represented sufficiently by a direct object property because the edge needs provenance, evidence, confidence, or additional qualifiers. The subject/predicate/object fields allow the association to be materialized as an RDF triple or property-graph edge.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:Association',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    predicate: str = Field(default=..., description="""Direct object property represented by this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'slot_uri': 'rdf:predicate'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class DiseasePhenotypeAssociation(Association):
    """
    Optional association for Disease -> Phenotype when the clinical feature requires edge metadata such as frequency, onset, severity, source cohort, or evidence. Materializes to disease_manifests_as_phenotype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:DiseasePhenotypeAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    has_disease: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:has_disease'} })
    has_phenotype: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:has_phenotype'} })
    predicate: Optional[str] = Field(default="alskb:disease_manifests_as_phenotype", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:disease_manifests_as_phenotype',
         'slot_uri': 'rdf:predicate'} })
    frequency: Optional[str] = Field(default=None, description="""Frequency in affected population or cohort""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:frequency'} })
    severity: Optional[str] = Field(default=None, description="""Typical severity or severity distribution""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype', 'DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:severity'} })
    onset_type: Optional[OnsetTypeEnum] = Field(default=None, description="""Onset pattern when phenotype is onset-specific""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:onset_type'} })
    cohort: Optional[str] = Field(default=None, description="""Cohort or study population supporting this phenotype annotation""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype', 'DiseasePhenotypeAssociation'],
         'slot_uri': 'alskb:cohort'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class GeneDiseaseAssociation(Association):
    """
    Optional association for Gene -> Disease when causal/risk/protective or correlative gene-disease edges need evidence, scores, statistics, or source-specific qualifiers. Materializes to gene_associated_with_disease.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:GeneDiseaseAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    has_gene: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation', 'GeneExpressionAssociation'],
         'slot_uri': 'alskb:has_gene'} })
    has_disease: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:has_disease'} })
    predicate: Optional[str] = Field(default="alskb:gene_associated_with_disease", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:gene_associated_with_disease',
         'slot_uri': 'rdf:predicate'} })
    association_type: Optional[str] = Field(default=None, description="""causal, risk_factor, protective, modifier, biomarker, or correlative""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:association_type'} })
    association_score: Optional[float] = Field(default=None, description="""Source-specific gene-disease association score""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation'], 'slot_uri': 'alskb:association_score'} })
    p_value: Optional[float] = Field(default=None, description="""Statistical significance when available""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation'], 'slot_uri': 'alskb:p_value'} })
    odds_ratio: Optional[float] = Field(default=None, description="""Genetic association odds ratio when available""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation', 'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:odds_ratio'} })
    effect_direction: Optional[str] = Field(default=None, description="""increased_risk, decreased_risk, protective, upregulated, downregulated, or unknown""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation'], 'slot_uri': 'alskb:effect_direction'} })
    evidence_count: Optional[int] = Field(default=None, description="""Number of supporting studies or records""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation'], 'slot_uri': 'alskb:evidence_count'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class VariantDiseaseAssociation(Association):
    """
    Optional association for Variant -> Disease when variant-level evidence, clinical significance, inheritance, penetrance, or source assertions are needed. Materializes to variant_associated_with_disease.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:VariantDiseaseAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    has_variant: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['VariantDiseaseAssociation', 'VariantProteinEffectAssociation'],
         'slot_uri': 'alskb:has_variant'} })
    has_disease: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:has_disease'} })
    predicate: Optional[str] = Field(default="alskb:variant_associated_with_disease", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:variant_associated_with_disease',
         'slot_uri': 'rdf:predicate'} })
    clinical_significance: Optional[str] = Field(default=None, description="""ClinVar/ACMG or ALS-specific clinical interpretation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Variant', 'VariantDiseaseAssociation'],
         'slot_uri': 'alskb:clinical_significance'} })
    inheritance_mode: Optional[str] = Field(default=None, description="""autosomal_dominant, autosomal_recessive, X_linked, mitochondrial, complex, or unknown""", json_schema_extra = { "linkml_meta": {'domain_of': ['VariantDiseaseAssociation'],
         'slot_uri': 'alskb:inheritance_mode'} })
    penetrance: Optional[str] = Field(default=None, description="""Complete, reduced, age-dependent, or unknown penetrance""", json_schema_extra = { "linkml_meta": {'domain_of': ['VariantDiseaseAssociation'], 'slot_uri': 'alskb:penetrance'} })
    association_type: Optional[str] = Field(default=None, description="""causal, risk_factor, modifier, protective, or uncertain""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:association_type'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class VariantProteinEffectAssociation(Association):
    """
    Optional association for Variant -> Protein when protein consequence, predicted effect, assay result, or functional evidence is needed. Materializes to variant_affects_protein.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:VariantProteinEffectAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    has_variant: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['VariantDiseaseAssociation', 'VariantProteinEffectAssociation'],
         'slot_uri': 'alskb:has_variant'} })
    has_protein: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['VariantProteinEffectAssociation'],
         'slot_uri': 'alskb:has_protein'} })
    predicate: Optional[str] = Field(default="alskb:variant_affects_protein", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:variant_affects_protein',
         'slot_uri': 'rdf:predicate'} })
    functional_consequence: Optional[str] = Field(default=None, description="""missense, frameshift, nonsense, splice_site, synonymous, repeat_expansion, or structural""", json_schema_extra = { "linkml_meta": {'domain_of': ['VariantProteinEffectAssociation'],
         'slot_uri': 'alskb:functional_consequence'} })
    predicted_effect: Optional[str] = Field(default=None, description="""loss_of_function, gain_of_function, dominant_negative, aggregation_prone, no_change, or unknown""", json_schema_extra = { "linkml_meta": {'domain_of': ['VariantProteinEffectAssociation'],
         'slot_uri': 'alskb:predicted_effect'} })
    assay: Optional[str] = Field(default=None, description="""Functional assay or computational method supporting the effect""", json_schema_extra = { "linkml_meta": {'domain_of': ['VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation'],
         'slot_uri': 'alskb:assay'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class ProteinProteinInteractionAssociation(Association):
    """
    Optional association for Protein -> Protein when interaction score, interaction type, database evidence, or assay metadata are needed. Materializes to protein_interacts_with_protein.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:ProteinProteinInteractionAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    protein_1: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinProteinInteractionAssociation'],
         'slot_uri': 'alskb:protein_1'} })
    protein_2: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinProteinInteractionAssociation'],
         'slot_uri': 'alskb:protein_2'} })
    predicate: Optional[str] = Field(default="alskb:protein_interacts_with_protein", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:protein_interacts_with_protein',
         'slot_uri': 'rdf:predicate'} })
    interaction_score: Optional[float] = Field(default=None, description="""Source-specific confidence score such as STRING combined score""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinProteinInteractionAssociation'],
         'slot_uri': 'alskb:interaction_score'} })
    interaction_type: Optional[str] = Field(default=None, description="""direct, indirect, physical, genetic, colocalization, pathway, or predicted""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinProteinInteractionAssociation'],
         'slot_uri': 'alskb:interaction_type'} })
    assay: Optional[str] = Field(default=None, description="""Assay or method supporting the interaction""", json_schema_extra = { "linkml_meta": {'domain_of': ['VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation'],
         'slot_uri': 'alskb:assay'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class DrugTargetAssociation(Association):
    """
    Optional association for Drug -> MolecularEntity when action type, binding affinity, target class, or mechanism evidence is needed. Materializes to drug_targets_molecular_entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:DrugTargetAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    has_drug: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DrugTargetAssociation', 'DrugDiseaseTherapeuticAssociation'],
         'slot_uri': 'alskb:has_drug'} })
    target: MolecularEntity = Field(default=..., description="""Gene or protein target""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugTargetAssociation'], 'slot_uri': 'alskb:target'} })
    predicate: Optional[str] = Field(default="alskb:drug_targets_molecular_entity", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:drug_targets_molecular_entity',
         'slot_uri': 'rdf:predicate'} })
    action_type: Optional[str] = Field(default=None, description="""inhibitor, activator, binder, antagonist, agonist, modulator, ASO_knockdown, or unknown""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugTargetAssociation'], 'slot_uri': 'alskb:action_type'} })
    binding_affinity_nm: Optional[float] = Field(default=None, description="""Binding affinity in nanomolar when available""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugTargetAssociation'],
         'slot_uri': 'alskb:binding_affinity_nm'} })
    mechanism: Optional[str] = Field(default=None, description="""Mechanistic description of target modulation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugTargetAssociation', 'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:mechanism'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class DrugDiseaseTherapeuticAssociation(Association):
    """
    Optional association for Drug -> Disease when therapeutic indication, approval status, clinical-trial evidence, or outcome metadata are needed. Materializes to drug_treats_or_modulates_disease.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:DrugDiseaseTherapeuticAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    has_drug: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DrugTargetAssociation', 'DrugDiseaseTherapeuticAssociation'],
         'slot_uri': 'alskb:has_drug'} })
    has_disease: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:has_disease'} })
    predicate: Optional[str] = Field(default="alskb:drug_treats_or_modulates_disease", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:drug_treats_or_modulates_disease',
         'slot_uri': 'rdf:predicate'} })
    relation_type: Optional[str] = Field(default=None, description="""treats, disease_modifying, symptomatic, palliative, contraindicated, off_label, or investigational""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticAssociation',
                       'DiseaseDiseaseAssociation'],
         'slot_uri': 'alskb:relation_type'} })
    approval_status: Optional[str] = Field(default=None, description="""approved, investigational, withdrawn, off_label, failed_trial, or unknown""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticAssociation'],
         'slot_uri': 'alskb:approval_status'} })
    clinical_phase: Optional[str] = Field(default=None, description="""Highest clinical development phase for ALS or ALS subtype""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticAssociation'],
         'slot_uri': 'alskb:clinical_phase'} })
    outcome_measure: Optional[str] = Field(default=None, description="""ALSFRS-R, survival, respiratory function, biomarker, or other endpoint""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticAssociation'],
         'slot_uri': 'alskb:outcome_measure'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class ExposureDiseaseAssociation(Association):
    """
    Optional association for ExposureOrStressor -> Disease when epidemiology, mechanism, dose, duration, population, or study design metadata are needed. Materializes to exposure_associated_with_disease.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:ExposureDiseaseAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    exposure: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureDiseaseAssociation'], 'slot_uri': 'alskb:exposure'} })
    has_disease: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:has_disease'} })
    predicate: Optional[str] = Field(default="alskb:exposure_associated_with_disease", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:exposure_associated_with_disease',
         'slot_uri': 'rdf:predicate'} })
    association_type: Optional[str] = Field(default=None, description="""risk_factor, protective, trigger, modifier, or correlative""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:association_type'} })
    mechanism: Optional[str] = Field(default=None, description="""Proposed biological mechanism""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugTargetAssociation', 'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:mechanism'} })
    epidemiological_support: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:epidemiological_support'} })
    odds_ratio: Optional[float] = Field(default=None, description="""Epidemiological odds ratio or equivalent effect estimate""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation', 'ExposureDiseaseAssociation'],
         'slot_uri': 'alskb:odds_ratio'} })
    population: Optional[str] = Field(default=None, description="""Population, geography, occupation, or cohort context""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureDiseaseAssociation'], 'slot_uri': 'alskb:population'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class TranscriptionFactorRegulationAssociation(Association):
    """
    Optional association for TranscriptionFactor -> Gene when direction, confidence, tissue/cell context, or assay evidence are needed. Materializes to transcription_factor_regulates_gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:TranscriptionFactorRegulationAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    transcription_factor: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactorRegulationAssociation'],
         'slot_uri': 'alskb:transcription_factor'} })
    target_gene: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactorRegulationAssociation'],
         'slot_uri': 'alskb:target_gene'} })
    predicate: Optional[str] = Field(default="alskb:transcription_factor_regulates_gene", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:transcription_factor_regulates_gene',
         'slot_uri': 'rdf:predicate'} })
    regulation_type: Optional[str] = Field(default=None, description="""activation, repression, bidirectional, context_dependent, or unknown""", json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactorRegulationAssociation'],
         'slot_uri': 'alskb:regulation_type'} })
    confidence_level: Optional[str] = Field(default=None, description="""Source-specific confidence level such as DoRothEA A-D""", json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactorRegulationAssociation'],
         'slot_uri': 'alskb:confidence_level'} })
    tissue_or_cell_type: Optional[str] = Field(default=None, description="""Tissue or cell type context for the regulatory relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation'],
         'slot_uri': 'alskb:tissue_or_cell_type'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class GeneExpressionAssociation(Association):
    """
    Optional association for Gene -> Anatomy when expression level, specificity, tissue, cell type, disease stage, or differential-expression qualifiers are needed. Materializes to gene_expressed_in_anatomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:GeneExpressionAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    has_gene: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiseaseAssociation', 'GeneExpressionAssociation'],
         'slot_uri': 'alskb:has_gene'} })
    has_anatomy: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAssociation'], 'slot_uri': 'alskb:has_anatomy'} })
    predicate: Optional[str] = Field(default="alskb:gene_expressed_in_anatomy", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:gene_expressed_in_anatomy',
         'slot_uri': 'rdf:predicate'} })
    expression_level: Optional[str] = Field(default=None, description="""high, medium, low, absent, upregulated, downregulated, or not_detected""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAssociation'],
         'slot_uri': 'alskb:expression_level'} })
    specificity_index: Optional[float] = Field(default=None, description="""Tissue-specificity score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAssociation'],
         'slot_uri': 'alskb:specificity_index'} })
    log2_fold_change: Optional[float] = Field(default=None, description="""Differential expression log2 fold change when available""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAssociation'],
         'slot_uri': 'alskb:log2_fold_change'} })
    adjusted_p_value: Optional[float] = Field(default=None, description="""Multiple-testing-adjusted p-value when available""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAssociation'],
         'slot_uri': 'alskb:adjusted_p_value'} })
    tissue_or_cell_type: Optional[str] = Field(default=None, description="""Tissue or cell-type context""", json_schema_extra = { "linkml_meta": {'domain_of': ['TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation'],
         'slot_uri': 'alskb:tissue_or_cell_type'} })
    disease_stage: Optional[str] = Field(default=None, description="""Disease stage or clinical context""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionAssociation'], 'slot_uri': 'alskb:disease_stage'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


class DiseaseDiseaseAssociation(Association):
    """
    Optional association for Disease -> Disease when disease-disease edges need relation type, similarity score, shared mechanism, or comorbidity statistics. Materializes to disease_related_to_disease.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskb:DiseaseDiseaseAssociation',
         'from_schema': 'https://alskb.org/ontology/als_kg'})

    disease_1: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseDiseaseAssociation'], 'slot_uri': 'alskb:disease_1'} })
    disease_2: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseDiseaseAssociation'], 'slot_uri': 'alskb:disease_2'} })
    predicate: Optional[str] = Field(default="alskb:disease_related_to_disease", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship',
                       'Association',
                       'DiseasePhenotypeAssociation',
                       'GeneDiseaseAssociation',
                       'VariantDiseaseAssociation',
                       'VariantProteinEffectAssociation',
                       'ProteinProteinInteractionAssociation',
                       'DrugTargetAssociation',
                       'DrugDiseaseTherapeuticAssociation',
                       'ExposureDiseaseAssociation',
                       'TranscriptionFactorRegulationAssociation',
                       'GeneExpressionAssociation',
                       'DiseaseDiseaseAssociation'],
         'ifabsent': 'alskb:disease_related_to_disease',
         'slot_uri': 'rdf:predicate'} })
    relation_type: Optional[str] = Field(default=None, description="""comorbidity, shared_pathway, shared_gene, phenotypic_similarity, differential_diagnosis, or disease_subtype""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticAssociation',
                       'DiseaseDiseaseAssociation'],
         'slot_uri': 'alskb:relation_type'} })
    similarity_score: Optional[float] = Field(default=None, description="""Semantic similarity or clinical overlap score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseDiseaseAssociation'],
         'slot_uri': 'alskb:similarity_score'} })
    shared_mechanism: Optional[str] = Field(default=None, description="""Shared biological mechanism, pathway, or clinical rationale""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseDiseaseAssociation'],
         'slot_uri': 'alskb:shared_mechanism'} })
    association_id: Optional[str] = Field(default=None, description="""Stable identifier for the association record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'schema:identifier'} })
    association_label: Optional[str] = Field(default=None, description="""Human-readable summary of the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Association'], 'slot_uri': 'rdfs:label'} })
    subject: str = Field(default=..., description="""Subject entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:subject'} })
    object: str = Field(default=..., description="""Object entity IRI or CURIE used to materialize a direct edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'rdf:object'} })
    source: Optional[str] = Field(default=None, description="""Data source for this association""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Relationship', 'Association'],
         'slot_uri': 'dcterms:source'} })
    source_version: Optional[str] = Field(default=None, description="""Data source version or release date""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Association'],
         'slot_uri': 'dcterms:hasVersion'} })
    evidence_type: Optional[str] = Field(default=None, description="""Type of supporting evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'ECO:0000000'} })
    evidence_source: Optional[str] = Field(default=None, description="""Publication, study, database record, or extraction artifact supporting the association""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'],
         'slot_uri': 'alskb:evidence_source'} })
    confidence: Optional[str] = Field(default=None, description="""Normalized confidence score from 0 to 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship', 'Association'], 'slot_uri': 'alskb:confidence'} })
    ingest_date: Optional[str] = Field(default=None, description="""Date this association was ingested""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass', 'Relationship', 'Association'],
         'slot_uri': 'alskb:ingest_date'} })
    last_updated: Optional[str] = Field(default=None, description="""Date this association was last modified""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity', 'Association'], 'slot_uri': 'dcterms:modified'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedEntity.model_rebuild()
OntologyClass.model_rebuild()
Relationship.model_rebuild()
DiseaseOrPhenotype.model_rebuild()
Disease.model_rebuild()
Phenotype.model_rebuild()
Anatomy.model_rebuild()
MolecularEntity.model_rebuild()
Gene.model_rebuild()
TranscriptionFactor.model_rebuild()
Protein.model_rebuild()
Variant.model_rebuild()
ChemicalEntity.model_rebuild()
Drug.model_rebuild()
ExposureOrStressor.model_rebuild()
BiologicalConcept.model_rebuild()
BiologicalProcess.model_rebuild()
MolecularFunction.model_rebuild()
CellularComponent.model_rebuild()
DiseaseSubtype.model_rebuild()
Association.model_rebuild()
DiseasePhenotypeAssociation.model_rebuild()
GeneDiseaseAssociation.model_rebuild()
VariantDiseaseAssociation.model_rebuild()
VariantProteinEffectAssociation.model_rebuild()
ProteinProteinInteractionAssociation.model_rebuild()
DrugTargetAssociation.model_rebuild()
DrugDiseaseTherapeuticAssociation.model_rebuild()
ExposureDiseaseAssociation.model_rebuild()
TranscriptionFactorRegulationAssociation.model_rebuild()
GeneExpressionAssociation.model_rebuild()
DiseaseDiseaseAssociation.model_rebuild()
