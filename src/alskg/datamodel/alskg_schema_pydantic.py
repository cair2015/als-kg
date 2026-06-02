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
version = "0.2.0-alskg-neo4j-extension"


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


linkml_meta = LinkMLMeta({'annotations': {'schema_role': {'tag': 'schema_role',
                                     'value': 'semantic_view'},
                     'standalone_schema': {'tag': 'standalone_schema',
                                           'value': 'true'}},
     'default_prefix': 'alskg',
     'default_range': 'string',
     'description': 'A LinkML schema for ALSKG that extends the OptimusKG semantic '
                    'model while preserving Neo4j-compatible node classes, '
                    'relationship classes, and graph semantics. It adds '
                    'ALS-focused classes and relationships for subtypes, variants, '
                    'pathogenesis, gene expression, cohorts, samples, assays, '
                    'evidence, biomarkers, model systems, therapy, and drug '
                    'repurposing.',
     'id': 'https://w3id.org/alskg/schema/alskg-schema',
     'imports': ['linkml:types', 'alskg_enums'],
     'license': 'MIT',
     'name': 'alskg_schema',
     'prefixes': {'BFO': {'prefix_prefix': 'BFO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/BFO_'},
                  'CHEMBL': {'prefix_prefix': 'CHEMBL',
                             'prefix_reference': 'https://www.ebi.ac.uk/chembl/compound_report_card/'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'DOI': {'prefix_prefix': 'DOI',
                          'prefix_reference': 'https://doi.org/'},
                  'DOID': {'prefix_prefix': 'DOID',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/DOID_'},
                  'DRUGBANK': {'prefix_prefix': 'DRUGBANK',
                               'prefix_reference': 'https://go.drugbank.com/drugs/'},
                  'ECO': {'prefix_prefix': 'ECO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/ECO_'},
                  'EFO': {'prefix_prefix': 'EFO',
                          'prefix_reference': 'http://www.ebi.ac.uk/efo/EFO_'},
                  'ENSG': {'prefix_prefix': 'ENSG',
                           'prefix_reference': 'https://ensembl.org/id/'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'HGNC': {'prefix_prefix': 'HGNC',
                           'prefix_reference': 'https://identifiers.org/hgnc/'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'IAO': {'prefix_prefix': 'IAO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/IAO_'},
                  'MESH': {'prefix_prefix': 'MESH',
                           'prefix_reference': 'http://id.nlm.nih.gov/mesh/'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'NCBIGene': {'prefix_prefix': 'NCBIGene',
                               'prefix_reference': 'https://identifiers.org/ncbigene/'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'ORPHANET': {'prefix_prefix': 'ORPHANET',
                               'prefix_reference': 'http://www.orpha.net/ORDO/Orphanet_'},
                  'PMID': {'prefix_prefix': 'PMID',
                           'prefix_reference': 'https://pubmed.ncbi.nlm.nih.gov/'},
                  'PR': {'prefix_prefix': 'PR',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/PR_'},
                  'REACT': {'prefix_prefix': 'REACT',
                            'prefix_reference': 'https://reactome.org/content/detail/'},
                  'RO': {'prefix_prefix': 'RO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/RO_'},
                  'RXNORM': {'prefix_prefix': 'RXNORM',
                             'prefix_reference': 'https://www.nlm.nih.gov/research/umls/rxnorm/'},
                  'SIO': {'prefix_prefix': 'SIO',
                          'prefix_reference': 'http://semanticscience.org/resource/'},
                  'SO': {'prefix_prefix': 'SO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/SO_'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'UniProtKB': {'prefix_prefix': 'UniProtKB',
                                'prefix_reference': 'https://identifiers.org/uniprot/'},
                  'alskg': {'prefix_prefix': 'alskg',
                            'prefix_reference': 'https://w3id.org/alskg/schema/'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'ensembl': {'prefix_prefix': 'ensembl',
                              'prefix_reference': 'https://identifiers.org/ensembl/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'obo': {'prefix_prefix': 'obo',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/'},
                  'okg': {'prefix_prefix': 'okg',
                          'prefix_reference': 'https://w3id.org/optimuskg/schema/'},
                  'optimuskg': {'prefix_prefix': 'optimuskg',
                                'prefix_reference': 'https://optimuskg.ai/schema/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'pav': {'prefix_prefix': 'pav',
                          'prefix_reference': 'http://purl.org/pav/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'uniprot': {'prefix_prefix': 'uniprot',
                              'prefix_reference': 'https://purl.uniprot.org/uniprot/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://arxiv.org/abs/2604.27269',
                  'https://doi.org/10.7910/DVN/IYNGEV',
                  'https://github.com/mims-harvard/optimuskg',
                  'https://optimuskg.ai',
                  'https://optimuskg.ai/docs/graph-schema/edges',
                  'https://optimuskg.ai/docs/graph-schema/nodes'],
     'source_file': 'src/alskg/schema/alskg_schema.yaml',
     'title': 'ALSKG Schema Extending OptimusKG',
     'types': {'Base64StringType': {'base': 'str',
                                    'description': 'A base64-encoded binary '
                                                   'payload stored as a string. '
                                                   'Used for mol_file_base64 and '
                                                   'mol_image_base64 on Drug '
                                                   'nodes.',
                                    'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
                                    'name': 'Base64StringType',
                                    'uri': 'xsd:string'},
               'CURIEType': {'base': 'str',
                             'description': 'A Compact URI (CURIE) identifier in '
                                            'the form {namespace}[:_]{local_id}. '
                                            'Examples: ENSG00000139618, '
                                            'GO:0000001, HP:0001250, '
                                            'MONDO:0005148. All namespace prefixes '
                                            'are validated against the Biolink '
                                            'Model namespace registry.',
                             'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
                             'name': 'CURIEType',
                             'uri': 'xsd:string'},
               'Probability': {'description': 'A probability-like score between 0 '
                                              'and 1.',
                               'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
                               'name': 'Probability',
                               'typeof': 'float'},
               'URIType': {'base': 'str',
                           'description': 'A URI or URL stored as a string.',
                           'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
                           'name': 'URIType',
                           'uri': 'xsd:anyURI'}}} )

class NodeLabelEnum(str, Enum):
    """
    Current three-letter OptimusKG Neo4j node labels.
    """
    ANA = "ANA"
    """
    Anatomy node label.
    """
    BPO = "BPO"
    """
    BiologicalProcess node label.
    """
    CCO = "CCO"
    """
    CellularComponent node label.
    """
    DIS = "DIS"
    """
    Disease node label.
    """
    DRG = "DRG"
    """
    Drug node label.
    """
    EXP = "EXP"
    """
    Exposure node label.
    """
    GEN = "GEN"
    """
    Gene node label.
    """
    MFN = "MFN"
    """
    MolecularFunction node label.
    """
    MST = "MST"
    """
    MolecularSubtype node label. Represents transcriptome-derived molecular disease subtypes defined by unsupervised multi-omic clustering (e.g. ALS-Ox, ALS-Glia, ALS-TE from the NYGC ALS Consortium). Not an ontology-derived class; uses a synthetic ALSMS ID scheme.
    """
    PHE = "PHE"
    """
    Phenotype node label.
    """
    PWY = "PWY"
    """
    Pathway node label.
    """
    ECX = "ECX"
    """
    GeneExpressionContext node label. Represents reified gene expression context nodes linking a gene, molecular subtype, tissue/anatomy, expression direction, and provenance into a single semantic unit.
    """
    ALS = "ALS"
    """
    ALS focal disease node label used if materializing AmyotrophicLateralSclerosis separately from DIS.
    """
    AST = "AST"
    """
    ALS subtype node.
    """
    CST = "CST"
    """
    Clinical subtype node.
    """
    GST = "GST"
    """
    Genetic subtype node.
    """
    PST = "PST"
    """
    Pathology subtype or pathogenesis statement node depending on local implementation; prefer PSTMT for PathogenesisStatement to avoid collision.
    """
    PGS = "PGS"
    """
    Progression subtype node.
    """
    SSC = "SSC"
    """
    Subtype scheme node.
    """
    SCR = "SCR"
    """
    Subtype criterion node.
    """
    VAR = "VAR"
    """
    Sequence variant node.
    """
    REX = "REX"
    """
    Repeat expansion node.
    """
    CLT = "CLT"
    """
    Cell type node.
    """
    PGM = "PGM"
    """
    Pathogenic mechanism node.
    """
    MEV = "MEV"
    """
    Molecular event node.
    """
    PAG = "PAG"
    """
    Protein aggregate node.
    """
    EST = "EST"
    """
    Evidence statement node.
    """
    PSTMT = "PSTMT"
    """
    Pathogenesis statement node.
    """
    DER = "DER"
    """
    Differential expression result node.
    """
    PAR = "PAR"
    """
    Protein abundance result node.
    """
    POB = "POB"
    """
    Phenotype observation node.
    """
    DST = "DST"
    """
    Disease stage node.
    """
    PRG = "PRG"
    """
    Progression pattern node.
    """
    BMK = "BMK"
    """
    Biomarker node.
    """
    STU = "STU"
    """
    Study node.
    """
    DAT = "DAT"
    """
    Dataset node.
    """
    COH = "COH"
    """
    Cohort node.
    """
    CMP = "CMP"
    """
    Comparator group node.
    """
    SMP = "SMP"
    """
    Sample node.
    """
    ASY = "ASY"
    """
    Assay node.
    """
    MOD = "MOD"
    """
    Model system node.
    """
    TX = "TX"
    """
    Therapeutic intervention node.
    """
    TRI = "TRI"
    """
    Clinical trial node.
    """
    DRH = "DRH"
    """
    Drug repurposing hypothesis node.
    """
    BAG = "BAG"
    """
    Biological agent node.
    """


class RelationshipTypeEnum(str, Enum):
    """
    Current Neo4j relationship type strings observed in the installed OptimusKG graph.
    """
    ACTIVATOR = "ACTIVATOR"
    """
    Drug activates the gene product or target associated with the gene.
    """
    ADVERSE_DRUG_REACTION = "ADVERSE_DRUG_REACTION"
    """
    Drug-to-phenotype relationship indicating an adverse drug reaction.
    """
    AGONIST = "AGONIST"
    """
    Drug acts as an agonist of the gene product or target associated with the gene.
    """
    ALLOSTERIC_ANTAGONIST = "ALLOSTERIC_ANTAGONIST"
    """
    Drug acts as an allosteric antagonist of the gene product or target associated with the gene.
    """
    ANTAGONIST = "ANTAGONIST"
    """
    Drug acts as an antagonist of the gene product or target associated with the gene.
    """
    ASSOCIATED_WITH = "ASSOCIATED_WITH"
    """
    Association relationship; generally evidence-bearing but not necessarily causal.
    """
    BINDING_AGENT = "BINDING_AGENT"
    """
    Drug binds the gene product or target associated with the gene.
    """
    BLOCKER = "BLOCKER"
    """
    Drug blocks the gene product or target associated with the gene.
    """
    CARRIER = "CARRIER"
    """
    Drug-gene relationship where the gene product is a carrier in pharmacologic context.
    """
    CONTRAINDICATION = "CONTRAINDICATION"
    """
    Drug is contraindicated for a disease or phenotype context.
    """
    DEGRADER = "DEGRADER"
    """
    Drug degrades or induces degradation of the gene product or target.
    """
    ENZYME = "ENZYME"
    """
    Drug-gene relationship where the gene product is an enzyme in drug metabolism or action context.
    """
    EXPRESSION_ABSENT = "EXPRESSION_ABSENT"
    """
    Gene expression is reported absent in an anatomical context.
    """
    EXPRESSION_PRESENT = "EXPRESSION_PRESENT"
    """
    Gene expression is reported present in an anatomical context.
    """
    INDICATION = "INDICATION"
    """
    Drug has an indicated therapeutic use for a disease, phenotype, or biological process context.
    """
    INHIBITOR = "INHIBITOR"
    """
    Drug inhibits the gene product or target associated with the gene.
    """
    INTERACTS_WITH = "INTERACTS_WITH"
    """
    Generic interaction or annotation-style relationship. Interpret according to the source and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    INVERSE_AGONIST = "INVERSE_AGONIST"
    """
    Drug acts as an inverse agonist of the gene product or target.
    """
    IS_A = "IS_A"
    """
    Ontology subclass relationship indicating the source concept is a kind of the target concept.
    """
    LINKED_TO = "LINKED_TO"
    """
    Generic linkage relation; interpret as associative rather than causal unless source evidence says otherwise.
    """
    MODULATOR = "MODULATOR"
    """
    Drug modulates the gene product or target associated with the gene.
    """
    NEGATIVE_ALLOSTERIC_MODULATOR = "NEGATIVE_ALLOSTERIC_MODULATOR"
    """
    Drug acts as a negative allosteric modulator of the gene product or target.
    """
    NEGATIVE_MODULATOR = "NEGATIVE_MODULATOR"
    """
    Drug negatively modulates the gene product or target.
    """
    OFF_LABEL_USE = "OFF_LABEL_USE"
    """
    Drug has off-label use for a disease or phenotype context.
    """
    OPENER = "OPENER"
    """
    Drug opens the gene product or target, often a channel target.
    """
    PARENT = "PARENT"
    """
    Parent-child hierarchy relationship from the source concept to a broader or parent concept in the same or related ontology.
    """
    PARTIAL_AGONIST = "PARTIAL_AGONIST"
    """
    Drug acts as a partial agonist of the gene product or target.
    """
    HAS_MOLECULAR_SUBTYPE = "HAS_MOLECULAR_SUBTYPE"
    """
    Disease-to-MolecularSubtype relationship indicating that a disease node is associated with or can present as a given molecular subtype. Direction is Disease -> MolecularSubtype. Not equivalent to ontological subclassing; represents a transcriptomic classification layer orthogonal to ontological disease hierarchy.
    """
    DYSREGULATED_IN = "DYSREGULATED_IN"
    """
    Gene-to-MolecularSubtype relationship indicating that a gene or genomic feature is differentially expressed (upregulated or downregulated) in a given molecular subtype relative to controls. Edge direction is Gene -> MolecularSubtype. Properties encode direction (UP/DOWN), tissue context (cortex or cord), and optionally cell model (e.g. iPSC motor neuron line).
    """
    MEASURED_IN = "MEASURED_IN"
    """
    MolecularSubtype-to-Anatomy relationship indicating the tissue or biological context in which the molecular subtype was characterized. Edge direction is MolecularSubtype -> Anatomy.
    """
    PHENOTYPE_PRESENT = "PHENOTYPE_PRESENT"
    """
    Disease-to-phenotype relationship indicating the phenotype is present in the disease context.
    """
    POSITIVE_ALLOSTERIC_MODULATOR = "POSITIVE_ALLOSTERIC_MODULATOR"
    """
    Drug acts as a positive allosteric modulator of the gene product or target.
    """
    POSITIVE_MODULATOR = "POSITIVE_MODULATOR"
    """
    Drug positively modulates the gene product or target.
    """
    RELEASING_AGENT = "RELEASING_AGENT"
    """
    Drug acts as a releasing agent affecting the gene product or related target system.
    """
    STABILISER = "STABILISER"
    """
    Drug stabilizes the gene product or target.
    """
    SUBSTRATE = "SUBSTRATE"
    """
    Drug is a substrate of the gene product, often an enzyme or transporter.
    """
    SYNERGISTIC_INTERACTION = "SYNERGISTIC_INTERACTION"
    """
    Drug-drug relationship indicating synergistic interaction.
    """
    TARGET = "TARGET"
    """
    Drug targets the gene product associated with the gene.
    """
    TRANSPORTER = "TRANSPORTER"
    """
    Drug-gene relationship where the gene product is a transporter in pharmacologic context.
    """
    HAS_EXPRESSION_CONTEXT = "HAS_EXPRESSION_CONTEXT"
    """
    Gene-to-GeneExpressionContext relationship. Links a gene to a reified expression context node that captures the molecular subtype, tissue/anatomy, expression direction, and provenance of a differential expression finding. Edge direction: Gene -> GeneExpressionContext.
    """
    IN_ANATOMY = "IN_ANATOMY"
    """
    GeneExpressionContext-to-Anatomy relationship. Links a reified expression context to the tissue or anatomical region in which the expression was measured. Optional: null when context is an iPSC cell model with no corresponding anatomy node. Edge direction: GeneExpressionContext -> Anatomy.
    """
    HAS_ALS_SUBTYPE = "HAS_ALS_SUBTYPE"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    IS_SUBTYPE_OF = "IS_SUBTYPE_OF"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    HAS_SUBTYPE_SCHEME = "HAS_SUBTYPE_SCHEME"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    HAS_SUBTYPE_CRITERION = "HAS_SUBTYPE_CRITERION"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    DEFINED_BY_GENE = "DEFINED_BY_GENE"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    DEFINED_BY_VARIANT = "DEFINED_BY_VARIANT"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    HAS_PATHOGENIC_MECHANISM = "HAS_PATHOGENIC_MECHANISM"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    AFFECTS_ANATOMY = "AFFECTS_ANATOMY"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    INVOLVES_CELL_TYPE = "INVOLVES_CELL_TYPE"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    HAS_PHENOTYPE_OBSERVATION = "HAS_PHENOTYPE_OBSERVATION"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    HAS_VARIANT = "HAS_VARIANT"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    AFFECTS_GENE = "AFFECTS_GENE"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    ALTERS_PROTEIN = "ALTERS_PROTEIN"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    CONTRIBUTES_TO_PATHOGENIC_MECHANISM = "CONTRIBUTES_TO_PATHOGENIC_MECHANISM"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    OCCURS_IN_CELL_TYPE = "OCCURS_IN_CELL_TYPE"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    OCCURS_IN_ANATOMY = "OCCURS_IN_ANATOMY"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    MEASURES_GENE_EXPRESSION_OF = "MEASURES_GENE_EXPRESSION_OF"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    OCCURS_IN_SUBTYPE_CONTEXT = "OCCURS_IN_SUBTYPE_CONTEXT"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    MEASURED_BY_ASSAY = "MEASURED_BY_ASSAY"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    DERIVES_FROM_DATASET = "DERIVES_FROM_DATASET"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    SUPPORTED_BY = "SUPPORTED_BY"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    HAS_OBSERVED_PHENOTYPE = "HAS_OBSERVED_PHENOTYPE"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    INDICATES_PATHOGENIC_MECHANISM = "INDICATES_PATHOGENIC_MECHANISM"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    PRIORITIZES_DRUG = "PRIORITIZES_DRUG"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    TARGETS_GENE = "TARGETS_GENE"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    MODULATES_PATHOGENIC_MECHANISM = "MODULATES_PATHOGENIC_MECHANISM"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    TESTED_IN_CLINICAL_TRIAL = "TESTED_IN_CLINICAL_TRIAL"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    ENROLLS_SUBTYPE = "ENROLLS_SUBTYPE"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """
    MODELS_SUBTYPE = "MODELS_SUBTYPE"
    """
    ALS-KG extension relationship type for Neo4j materialization.
    """


class GeneBiotypeEnum(str, Enum):
    """
    Gene biotype classifications from HGNC/Ensembl, stored on Gene nodes.
    """
    protein_coding = "protein_coding"
    """
    Protein-coding gene
    """
    lncRNA = "lncRNA"
    """
    Long non-coding RNA
    """
    miRNA = "miRNA"
    """
    MicroRNA
    """
    snRNA = "snRNA"
    """
    Small nuclear RNA
    """
    snoRNA = "snoRNA"
    """
    Small nucleolar RNA
    """
    rRNA = "rRNA"
    """
    Ribosomal RNA
    """
    tRNA = "tRNA"
    """
    Transfer RNA
    """
    pseudogene = "pseudogene"
    """
    Pseudogene
    """
    misc_RNA = "misc_RNA"
    """
    Miscellaneous RNA
    """
    other = "other"
    """
    Other or unclassified biotype
    """


class ExpressionCallQualityEnum(str, Enum):
    """
    Bgee expression call quality levels for ANA-GEN edges. Reflects confidence in gene expression calls derived from curated RNA-seq data.
    """
    gold = "gold"
    """
    High-confidence expression call (multiple concordant evidence types)
    """
    silver = "silver"
    """
    Moderate-confidence expression call
    """


class DrugTractabilityModalityEnum(str, Enum):
    """
    Drug discovery modality categories for tractability assessments on Gene nodes. Sourced from Open Targets tractability pipeline.
    """
    sm = "sm"
    """
    Small molecule modality
    """
    ab = "ab"
    """
    Antibody modality
    """
    pr = "pr"
    """
    PROTAC (protein degrader) modality
    """
    oc = "oc"
    """
    Other clinical modality
    """


class HomologyTypeEnum(str, Enum):
    """
    Types of homology relationships in gene homologue annotations on Gene nodes.
    """
    ortholog_one2one = "ortholog_one2one"
    """
    One-to-one ortholog (single copy in both species)
    """
    ortholog_one2many = "ortholog_one2many"
    """
    One-to-many ortholog
    """
    ortholog_many2many = "ortholog_many2many"
    """
    Many-to-many ortholog
    """
    within_species_paralog = "within_species_paralog"
    """
    Paralog within the same species
    """
    other_paralog = "other_paralog"
    """
    Other paralogous relationship
    """
    gene_split = "gene_split"
    """
    Split gene (fragment)
    """


class ExpressionDirectionEnum(str, Enum):
    """
    Direction of differential expression relative to a comparator. Includes legacy OptimusKG values UP/DOWN and semantic ALS-KG values increased/decreased/unchanged/mixed/unknown.
    """
    UP = "UP"
    """
    Gene or feature is upregulated (higher expression) in the molecular subtype compared to non-ALS controls.
    """
    DOWN = "DOWN"
    """
    Gene or feature is downregulated (lower expression) in the molecular subtype compared to non-ALS controls.
    """
    increased = "increased"
    """
    Expression is higher in the case or condition group than in the comparator group.
    """
    decreased = "decreased"
    """
    Expression is lower in the case or condition group than in the comparator group.
    """
    unchanged = "unchanged"
    """
    No statistically meaningful expression change is observed.
    """
    mixed = "mixed"
    """
    Direction differs across cohorts, cell types, tissues, assays, or analytical methods.
    """
    unknown = "unknown"
    """
    Direction is not specified or cannot be determined.
    """


class BiologicalContextTypeEnum(str, Enum):
    """
    Type of biological context (tissue or cell model) in which molecular subtype gene expression was measured. Used on DYSREGULATED_IN edges.
    """
    postmortem_cortex = "postmortem_cortex"
    """
    Human postmortem motor cortex tissue sample.
    """
    postmortem_cord = "postmortem_cord"
    """
    Human postmortem spinal cord tissue sample.
    """
    iPSC_motor_neuron = "iPSC_motor_neuron"
    """
    iPSC-derived induced motor neuron cell model.
    """
    C9orf72_motor_neuron = "C9orf72_motor_neuron"
    """
    iPSC motor neuron model carrying C9orf72 repeat expansion mutation.
    """
    FUS_motor_neuron = "FUS_motor_neuron"
    """
    iPSC motor neuron model carrying FUS mutation.
    """
    TDP43_motor_neuron = "TDP43_motor_neuron"
    """
    iPSC motor neuron model carrying TARDBP/TDP-43 mutation.
    """
    spinal_cord_cervical = "spinal_cord_cervical"
    """
    Human postmortem cervical spinal cord tissue sample.
    """
    spinal_cord_thoracic = "spinal_cord_thoracic"
    """
    Human postmortem thoracic spinal cord tissue sample.
    """
    spinal_cord_lumbar = "spinal_cord_lumbar"
    """
    Human postmortem lumbar spinal cord tissue sample.
    """


class MolecularSubtypeClassificationBasisEnum(str, Enum):
    """
    Computational or experimental basis used to define and assign molecular subtypes. Describes how the subtype was derived from raw data.
    """
    unsupervised_transcriptomics = "unsupervised_transcriptomics"
    """
    Molecular subtype derived by unsupervised clustering of postmortem transcriptomes (e.g. k-means, hierarchical clustering, NMF).
    """
    deep_multiomics_classifier = "deep_multiomics_classifier"
    """
    Molecular subtype assigned by a deep learning multi-omics classifier (e.g. the DANCer neural network from the NYGC ALS Consortium, Cell Reports 2025).
    """
    bootstrap_clustering = "bootstrap_clustering"
    """
    Subtype assigned via bootstrap-based resampling and clustering stability analysis.
    """


class SubtypeAxisEnum(str, Enum):
    """
    Axes along which ALS subtypes may be defined.
    """
    clinical_onset = "clinical_onset"
    """
    Subtype based on site or pattern of clinical onset, such as bulbar-onset or limb-onset ALS.
    """
    motor_neuron_involvement = "motor_neuron_involvement"
    """
    Subtype based on upper and lower motor neuron involvement pattern.
    """
    genetic = "genetic"
    """
    Subtype based on a gene, variant, repeat expansion, or inherited/genetic cause.
    """
    molecular = "molecular"
    """
    Subtype derived from molecular data such as transcriptomics, proteomics, epigenomics, or multi-omics.
    """
    pathology = "pathology"
    """
    Subtype based on pathological findings such as TDP-43, SOD1, or FUS proteinopathy.
    """
    cognitive_behavioral = "cognitive_behavioral"
    """
    Subtype based on cognitive or behavioral features such as ALS-FTD.
    """
    progression = "progression"
    """
    Subtype based on progression speed, survival, or functional decline.
    """
    anatomical = "anatomical"
    """
    Subtype based on dominant anatomical system or region affected.
    """
    model_system = "model_system"
    """
    Subtype or disease model defined in an experimental model system.
    """


class EvidenceStrengthEnum(str, Enum):
    """
    Qualitative evidence strength for a scientific assertion.
    """
    definitive = "definitive"
    """
    Strongly supported by replicated, high-quality evidence or accepted clinical/genetic evidence.
    """
    strong = "strong"
    """
    Supported by substantial evidence from curated, experimental, or replicated sources.
    """
    moderate = "moderate"
    """
    Supported by some evidence, but with limitations or limited replication.
    """
    weak = "weak"
    """
    Supported by limited or preliminary evidence.
    """
    conflicting = "conflicting"
    """
    Evidence is inconsistent across studies or modalities.
    """
    unknown = "unknown"
    """
    Evidence strength has not been assessed.
    """


class EvidenceModalityEnum(str, Enum):
    """
    Modality or source type of evidence supporting a statement.
    """
    clinical = "clinical"
    """
    Evidence from clinical observations, examinations, diagnostic records, or clinical cohorts.
    """
    genetic = "genetic"
    """
    Evidence from genetic association, segregation, variant interpretation, or sequencing studies.
    """
    transcriptomic = "transcriptomic"
    """
    Evidence from RNA-seq, single-cell RNA-seq, spatial transcriptomics, microarray, or related assays.
    """
    proteomic = "proteomic"
    """
    Evidence from protein abundance, localization, aggregation, or post-translational modification assays.
    """
    pathology = "pathology"
    """
    Evidence from histology, immunostaining, digital pathology, or neuropathological assessment.
    """
    biomarker = "biomarker"
    """
    Evidence from molecular, imaging, electrophysiological, or clinical biomarkers.
    """
    experimental_model = "experimental_model"
    """
    Evidence from animal, cell, iPSC, organoid, or other model systems.
    """
    literature_curated = "literature_curated"
    """
    Evidence curated from scientific literature.
    """
    database_curated = "database_curated"
    """
    Evidence curated from a database or knowledge base.
    """
    computational_prediction = "computational_prediction"
    """
    Evidence generated by computational model, embedding, machine learning, or algorithmic inference.
    """


class VariantConsequenceEnum(str, Enum):
    """
    Broad variant consequence categories relevant to ALS.
    """
    repeat_expansion = "repeat_expansion"
    """
    Pathogenic or potentially pathogenic repeat expansion.
    """
    missense_variant = "missense_variant"
    """
    Variant causing an amino-acid substitution.
    """
    nonsense_variant = "nonsense_variant"
    """
    Variant introducing a premature stop codon.
    """
    frameshift_variant = "frameshift_variant"
    """
    Insertion/deletion that shifts the coding frame.
    """
    splice_region_variant = "splice_region_variant"
    """
    Variant affecting splice region or splicing.
    """
    noncoding_variant = "noncoding_variant"
    """
    Variant located outside coding sequence.
    """
    structural_variant = "structural_variant"
    """
    Larger deletion, duplication, inversion, insertion, or translocation.
    """
    copy_number_variant = "copy_number_variant"
    """
    Copy number gain or loss.
    """
    unknown = "unknown"
    """
    Consequence is not known.
    """


class PathogenicityEnum(str, Enum):
    """
    Clinical or research pathogenicity interpretation of a genetic variant.
    """
    pathogenic = "pathogenic"
    """
    Variant is interpreted as disease-causing.
    """
    likely_pathogenic = "likely_pathogenic"
    """
    Variant is likely disease-causing.
    """
    risk_factor = "risk_factor"
    """
    Variant is associated with increased disease risk but may not be fully penetrant or causal alone.
    """
    uncertain_significance = "uncertain_significance"
    """
    Variant has uncertain pathogenic significance.
    """
    likely_benign = "likely_benign"
    """
    Variant is likely benign.
    """
    benign = "benign"
    """
    Variant is benign.
    """
    unknown = "unknown"
    """
    Pathogenicity is not known.
    """


class PathogenicMechanismEnum(str, Enum):
    """
    Major ALS pathogenic mechanism categories.
    """
    TDP43_proteinopathy = "TDP43_proteinopathy"
    """
    TDP-43 mislocalization, aggregation, loss of nuclear function, or gain of toxic function.
    """
    SOD1_toxicity = "SOD1_toxicity"
    """
    Toxic gain of function, aggregation, or dysfunction related to SOD1.
    """
    FUS_proteinopathy = "FUS_proteinopathy"
    """
    FUS mislocalization, aggregation, or RNA-binding dysfunction.
    """
    C9orf72_repeat_toxicity = "C9orf72_repeat_toxicity"
    """
    Toxicity related to C9orf72 repeat expansion, RNA foci, DPR proteins, or haploinsufficiency.
    """
    RNA_processing_dysfunction = "RNA_processing_dysfunction"
    """
    Disrupted RNA splicing, transport, stability, translation, or RNA granule biology.
    """
    impaired_proteostasis = "impaired_proteostasis"
    """
    Protein quality control, ubiquitin-proteasome, autophagy, or lysosomal dysfunction.
    """
    mitochondrial_dysfunction = "mitochondrial_dysfunction"
    """
    Mitochondrial impairment, energy metabolism dysfunction, or mitochondrial stress.
    """
    oxidative_stress = "oxidative_stress"
    """
    Oxidative damage or disrupted redox homeostasis.
    """
    neuroinflammation = "neuroinflammation"
    """
    Inflammatory processes involving microglia, astrocytes, peripheral immune cells, complement, or cytokines.
    """
    glutamate_excitotoxicity = "glutamate_excitotoxicity"
    """
    Excitotoxic injury involving glutamate signaling or uptake.
    """
    axonal_transport_defect = "axonal_transport_defect"
    """
    Defect in axonal transport, cytoskeletal dynamics, or neuromuscular connectivity.
    """
    nucleocytoplasmic_transport_defect = "nucleocytoplasmic_transport_defect"
    """
    Disrupted nuclear-cytoplasmic transport or nuclear pore biology.
    """
    DNA_repair_defect = "DNA_repair_defect"
    """
    Defect in DNA damage response or genome maintenance.
    """
    metabolic_dysfunction = "metabolic_dysfunction"
    """
    Altered metabolic state, lipid metabolism, or energy homeostasis.
    """
    neuromuscular_junction_dysfunction = "neuromuscular_junction_dysfunction"
    """
    Pathological change at the neuromuscular junction.
    """
    other = "other"
    """
    Other pathogenic mechanism not covered by the listed categories.
    """


class DrugActionDirectionEnum(str, Enum):
    """
    Direction or mechanism of a drug action on a target or biological process.
    """
    inhibits = "inhibits"
    """
    Drug decreases activity or function of the target.
    """
    activates = "activates"
    """
    Drug increases activity or function of the target.
    """
    antagonizes = "antagonizes"
    """
    Drug blocks receptor or target activation.
    """
    agonizes = "agonizes"
    """
    Drug activates receptor or target signaling.
    """
    modulates = "modulates"
    """
    Drug modulates the target without specifying direction.
    """
    degrades = "degrades"
    """
    Drug promotes degradation of the target.
    """
    stabilizes = "stabilizes"
    """
    Drug stabilizes the target, complex, or functional state.
    """
    binds = "binds"
    """
    Drug binds the target, direction not specified.
    """
    unknown = "unknown"
    """
    Drug action is not specified.
    """


class RepurposingStatusEnum(str, Enum):
    """
    Status of a drug repurposing hypothesis.
    """
    proposed = "proposed"
    """
    Hypothesis is proposed based on KG, literature, omics, or computational evidence.
    """
    prioritized = "prioritized"
    """
    Hypothesis has been ranked or prioritized for further study.
    """
    experimentally_supported = "experimentally_supported"
    """
    Hypothesis has supporting experimental-model evidence.
    """
    clinically_tested = "clinically_tested"
    """
    Hypothesis has been evaluated in a clinical trial or observational clinical study.
    """
    deprioritized = "deprioritized"
    """
    Hypothesis is deprioritized because of weak evidence, wrong direction, toxicity, or lack of feasibility.
    """
    rejected = "rejected"
    """
    Hypothesis is rejected based on negative or contradictory evidence.
    """


class SexEnum(str, Enum):
    """
    Biological sex or sex category used in a study or observation when reported.
    """
    female = "female"
    """
    Female.
    """
    male = "male"
    """
    Male.
    """
    mixed = "mixed"
    """
    Mixed or combined sex groups.
    """
    unknown = "unknown"
    """
    Sex not reported or unknown.
    """



class NamedEntity(ConfiguredBaseModel):
    """
    Root abstract class for all named entities in OptimusKG. Replaces the former BiomedicalEntity root (v0.3.0). Provides core identity slots shared across all four mid-tier branches: OntologyClass, ClinicalEntity, PhysicalEntity, and AnalyticalEntity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:NamedThing',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class OntologyClass(NamedEntity):
    """
    Abstract mid-tier for entity types grounded in an OBO/OWL ontology or curated pathway database. All subclasses carry ontology header metadata (title, version, license, definition) and cross-references. Covers: Anatomy (Uberon), BiologicalProcess (GO), CellularComponent (GO), MolecularFunction (GO), Pathway (Reactome).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'owl:Class',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction'],
         'slot_uri': 'IAO:0000115'} })
    synonyms: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Drug',
                       'MolecularFunction'],
         'slot_uri': 'skos:altLabel'} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    ontology: Optional[str] = Field(default=None, description="""Metadata about the source ontology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction',
                       'Phenotype']} })


class ClinicalEntity(NamedEntity):
    """
    Abstract mid-tier for clinical observation categories grounded in disease and phenotype ontologies. Both subclasses carry UMLS CUIs, SNOMED CT mappings, and full ontological hierarchy (parents, ancestors, is_leaf). Covers: Disease (MONDO, DOID, EFO, Orphanet, NCIT), Phenotype (HPO, MedDRA).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:DiseaseOrPhenotypicFeature',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class PhysicalEntity(NamedEntity):
    """
    Abstract mid-tier for physically real, structurally defined entities whose identity is established by a structure or sequence database (not by an ontology concept hierarchy). Merges the former MolecularEntity (Gene, Protein) and ChemicalEntity (Drug, Exposure) branches into one family. Biolink alignment: biolink:ChemicalEntityOrGeneOrGeneProduct covers this combined family. Covers: Gene (ENSG), Protein (UniProt), Drug (ChEMBL/DrugBank/RxNorm), Exposure (MeSH/CTD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:ChemicalEntityOrGeneOrGeneProduct',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class AnalyticalEntity(NamedEntity):
    """
    Abstract mid-tier for entities whose identity is established by a computational analysis rather than an ontology or physical database. These are reified analytical findings promoted to named nodes because they accumulate enough properties and relationships to warrant first-class graph identity. Covers: MolecularSubtype (transcriptomic patient strata, MST label), GeneExpressionContext (reified differential expression findings, ECX label).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:StudyResult',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class Anatomy(AnalyticalEntity):
    """
    An anatomical entity or anatomical region represented in OptimusKG. Current Neo4j label: `ANA`.

    Property detail from OptimusKG source schema: An anatomical structure or tissue node. Represents 13,120 anatomical entities (6.9% of nodes) from the Uberon cross-species anatomy ontology. Covers organs, tissues, cell types, developmental structures, and systems. Source: Uberon. Node file: nodes/anatomy.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'ANA'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'ANA'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'AnatomyNode'}},
         'class_uri': 'biolink:AnatomicalEntity',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'definition': {'description': 'Formal ontology definition of '
                                                      'the anatomical structure',
                                       'name': 'definition'},
                        'name': {'description': 'Anatomical structure name (Uberon '
                                                'preferred label, e.g. "heart", '
                                                '"liver")',
                                 'name': 'name',
                                 'range': 'string'},
                        'ontology': {'description': 'Source ontology metadata (Uberon '
                                                    'title, version, license)',
                                     'name': 'ontology'},
                        'synonyms': {'description': 'Alternative anatomical names and '
                                                    'labels (e.g. abbreviations, Latin '
                                                    'names, synonymous tissue terms)',
                                     'name': 'synonyms'},
                        'xrefs': {'description': 'Cross-references to external '
                                                 'ontologies and databases (e.g. FMA, '
                                                 'MA, EHDAA2, BTO, OpenGalen, '
                                                 'Wikipedia)',
                                  'name': 'xrefs'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Anatomical structure name (Uberon preferred label, e.g. \"heart\", \"liver\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    definition: Optional[str] = Field(default=None, description="""Formal ontology definition of the anatomical structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction'],
         'slot_uri': 'IAO:0000115'} })
    synonyms: Optional[list[str]] = Field(default=None, description="""Alternative anatomical names and labels (e.g. abbreviations, Latin names, synonymous tissue terms)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Drug',
                       'MolecularFunction'],
         'slot_uri': 'skos:altLabel'} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external ontologies and databases (e.g. FMA, MA, EHDAA2, BTO, OpenGalen, Wikipedia)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    ontology: Optional[str] = Field(default=None, description="""Source ontology metadata (Uberon title, version, license)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction',
                       'Phenotype']} })


class BiologicalProcess(OntologyClass):
    """
    A Gene Ontology biological process term represented in OptimusKG. Current Neo4j label: `BPO`.

    Property detail from OptimusKG source schema: A Gene Ontology (GO) biological process node. Represents 25,754 biological processes (13.5% of nodes) describing coordinated programs of molecular activities with a defined beginning and end (e.g. \"apoptotic process\", \"DNA repair\", \"cell division\"). Source: Gene Ontology (GO). Node file: nodes/biological_process.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'BPO'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'BPO'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'BiologicalProcessNode'}},
         'class_uri': 'biolink:BiologicalProcess',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'definition': {'description': 'Formal GO ontology definition '
                                                      'of the biological process',
                                       'name': 'definition'},
                        'name': {'description': 'GO biological process name (e.g. '
                                                '"apoptotic process")',
                                 'name': 'name',
                                 'range': 'string'},
                        'ontology': {'description': 'Source ontology metadata (GO '
                                                    'title, version, license)',
                                     'name': 'ontology'},
                        'synonyms': {'description': 'Alternative GO term names and '
                                                    'synonyms',
                                     'name': 'synonyms'},
                        'xrefs': {'description': 'Cross-references to external '
                                                 'databases (e.g. KEGG, Reactome, '
                                                 'Wikipedia)',
                                  'name': 'xrefs'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""GO biological process name (e.g. \"apoptotic process\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    definition: Optional[str] = Field(default=None, description="""Formal GO ontology definition of the biological process""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction'],
         'slot_uri': 'IAO:0000115'} })
    synonyms: Optional[list[str]] = Field(default=None, description="""Alternative GO term names and synonyms""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Drug',
                       'MolecularFunction'],
         'slot_uri': 'skos:altLabel'} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external databases (e.g. KEGG, Reactome, Wikipedia)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    ontology: Optional[str] = Field(default=None, description="""Source ontology metadata (GO title, version, license)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction',
                       'Phenotype']} })


class CellularComponent(OntologyClass):
    """
    A Gene Ontology cellular component term represented in OptimusKG. Current Neo4j label: `CCO`.

    Property detail from OptimusKG source schema: A Gene Ontology (GO) cellular component node. Represents 4,052 subcellular structures and compartments (2.1% of nodes) where gene products are active or located (e.g. \"nucleus\", \"mitochondria\", \"plasma membrane\", \"ribosome\"). Source: Gene Ontology (GO). Node file: nodes/cellular_component.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'CCO'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'CCO'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'CellularComponentNode'}},
         'class_uri': 'biolink:CellularComponent',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'definition': {'description': 'Formal GO ontology definition',
                                       'name': 'definition'},
                        'name': {'description': 'GO cellular component name (e.g. '
                                                '"cytoplasm", "nucleus")',
                                 'name': 'name',
                                 'range': 'string'},
                        'ontology': {'description': 'Source ontology metadata (GO '
                                                    'title, version, license)',
                                     'name': 'ontology'},
                        'synonyms': {'description': 'Alternative GO term names and '
                                                    'synonyms',
                                     'name': 'synonyms'},
                        'xrefs': {'description': 'Cross-references to external '
                                                 'databases',
                                  'name': 'xrefs'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""GO cellular component name (e.g. \"cytoplasm\", \"nucleus\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    definition: Optional[str] = Field(default=None, description="""Formal GO ontology definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction'],
         'slot_uri': 'IAO:0000115'} })
    synonyms: Optional[list[str]] = Field(default=None, description="""Alternative GO term names and synonyms""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Drug',
                       'MolecularFunction'],
         'slot_uri': 'skos:altLabel'} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    ontology: Optional[str] = Field(default=None, description="""Source ontology metadata (GO title, version, license)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction',
                       'Phenotype']} })


class Disease(ClinicalEntity):
    """
    A disease, disorder, or clinical condition represented in OptimusKG. Current Neo4j label: `DIS`.

    Property detail from OptimusKG source schema: A human disease node. Represents 36,345 diseases (19.1% of nodes) spanning genetic, infectious, cancer, environmental, complex, rare, and common human diseases. Harmonized across MONDO, DOID, EFO, Orphanet, NCIT, and other ontologies with full hierarchical structure. Sources: DrugCentral, Mondo, Open Targets. Node file: nodes/disease.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'DIS'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'DIS'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'DiseaseNode'}},
         'class_uri': 'biolink:Disease',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'ancestors': {'description': 'All transitive ancestor '
                                                     '(parent-of-parent-of-...) '
                                                     'disease term IDs',
                                      'name': 'ancestors'},
                        'broad_synonyms': {'description': 'Broader term synonyms (more '
                                                          'general concepts)',
                                           'name': 'broad_synonyms'},
                        'children': {'description': 'Direct child disease term '
                                                    'identifiers',
                                     'name': 'children'},
                        'code': {'description': 'Primary ontology code / identifier '
                                                'for the disease term',
                                 'name': 'code'},
                        'concept_ids': {'description': 'UMLS concept IDs (CUIs) linked '
                                                       'to this disease',
                                        'name': 'concept_ids'},
                        'concept_names': {'description': 'UMLS concept names '
                                                         'corresponding to concept_ids',
                                          'name': 'concept_names'},
                        'cui_semantic_type': {'description': 'UMLS semantic type for '
                                                             'the primary CUI (e.g. '
                                                             '"Disease or Syndrome", '
                                                             '"Neoplastic Process").',
                                              'name': 'cui_semantic_type'},
                        'descendants': {'description': 'All transitive descendant '
                                                       '(child-of-child-of-...) '
                                                       'disease term IDs',
                                        'name': 'descendants'},
                        'description': {'description': 'Free-text disease description '
                                                       'from the ontology definition',
                                        'name': 'description'},
                        'exact_synonyms': {'description': 'Exact lexical synonyms '
                                                          '(same meaning, different '
                                                          'spelling/abbreviation)',
                                           'name': 'exact_synonyms'},
                        'is_leaf': {'description': 'True if this disease term has no '
                                                   'children (leaf node in ontology '
                                                   'tree)',
                                    'name': 'is_leaf'},
                        'name': {'description': 'Primary disease name (preferred label '
                                                'in the source ontology)',
                                 'name': 'name',
                                 'range': 'string'},
                        'narrow_synonyms': {'description': 'Narrower term synonyms '
                                                           '(more specific concepts)',
                                            'name': 'narrow_synonyms'},
                        'obsolete_terms': {'description': 'Deprecated or retired '
                                                          'disease term labels',
                                           'name': 'obsolete_terms'},
                        'obsolete_xrefs': {'description': 'Deprecated cross-references '
                                                          'to external databases',
                                           'name': 'obsolete_xrefs'},
                        'parents': {'description': 'Direct parent disease term '
                                                   'identifiers in the ontology '
                                                   'hierarchy. Enables traversal of '
                                                   'the disease DAG (directed acyclic '
                                                   'graph).',
                                    'name': 'parents'},
                        'related_synonyms': {'description': 'Semantically related '
                                                            'synonyms (close but not '
                                                            'exact meaning)',
                                             'name': 'related_synonyms'},
                        'snomed_concept_ids': {'description': 'SNOMED CT concept '
                                                              'identifiers',
                                               'name': 'snomed_concept_ids'},
                        'snomed_full_names': {'description': 'SNOMED CT preferred full '
                                                             'concept names',
                                              'name': 'snomed_full_names'},
                        'umls_cui': {'description': 'Primary UMLS Concept Unique '
                                                    'Identifier (CUI) for this '
                                                    'disease. Key cross-reference for '
                                                    'integration with clinical NLP '
                                                    'systems.',
                                     'name': 'umls_cui'},
                        'xrefs': {'description': 'Cross-references to external '
                                                 'databases (e.g. ICD-10, OMIM, MeSH, '
                                                 'MedDRA). Formatted as CURIE strings.',
                                  'name': 'xrefs'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Primary disease name (preferred label in the source ontology)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    disease_has_molecular_subtype: Optional[str] = Field(default=None, description="""Current OptimusKG Neo4j relationship `HAS_MOLECULAR_SUBTYPE` from `DIS`/Disease to `MST`/MolecularSubtype. Indicates that a disease node is associated with a transcriptome-derived molecular subtype. Orthogonal to the ontological disease hierarchy; represents a classification layer derived from unsupervised multi-omic clustering.""", json_schema_extra = { "linkml_meta": {'annotations': {'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'MST'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_MOLECULAR_SUBTYPE'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DIS'}},
         'domain': 'Disease',
         'domain_of': ['Disease'],
         'slot_uri': 'okg:has_molecular_subtype'} })
    has_als_subtype: Optional[list[str]] = Field(default=None, description="""Connects ALS disease to an ALS subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'AmyotrophicLateralSclerosis'],
         'slot_uri': 'alskg:has_subtype'} })
    has_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects ALS, an ALS subtype, or an assertion to a pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_pathogenic_mechanism'} })
    has_phenotype_observation: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_phenotype_observation'} })
    affects_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or result to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'RO:0002131'} })
    involves_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or observation to a relevant cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'alskg:involves_cell_type'} })
    disease_has_als_subtype: Optional[str] = Field(default=None, description="""Disease-to-subtype relationship meaning the disease has the ALS subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'alskg:disease_has_als_subtype'} })
    description: Optional[str] = Field(default=None, description="""Free-text disease description from the ontology definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    code: Optional[str] = Field(default=None, description="""Primary ontology code / identifier for the disease term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    parents: Optional[list[str]] = Field(default=None, description="""Direct parent disease term identifiers in the ontology hierarchy. Enables traversal of the disease DAG (directed acyclic graph).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    children: Optional[list[str]] = Field(default=None, description="""Direct child disease term identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    ancestors: Optional[list[str]] = Field(default=None, description="""All transitive ancestor (parent-of-parent-of-...) disease term IDs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    descendants: Optional[list[str]] = Field(default=None, description="""All transitive descendant (child-of-child-of-...) disease term IDs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    is_leaf: Optional[bool] = Field(default=None, description="""True if this disease term has no children (leaf node in ontology tree)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    exact_synonyms: Optional[list[str]] = Field(default=None, description="""Exact lexical synonyms (same meaning, different spelling/abbreviation)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    related_synonyms: Optional[list[str]] = Field(default=None, description="""Semantically related synonyms (close but not exact meaning)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    narrow_synonyms: Optional[list[str]] = Field(default=None, description="""Narrower term synonyms (more specific concepts)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    broad_synonyms: Optional[list[str]] = Field(default=None, description="""Broader term synonyms (more general concepts)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    obsolete_terms: Optional[list[str]] = Field(default=None, description="""Deprecated or retired disease term labels""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    obsolete_xrefs: Optional[list[str]] = Field(default=None, description="""Deprecated cross-references to external databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external databases (e.g. ICD-10, OMIM, MeSH, MedDRA). Formatted as CURIE strings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    concept_ids: Optional[list[str]] = Field(default=None, description="""UMLS concept IDs (CUIs) linked to this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    concept_names: Optional[list[str]] = Field(default=None, description="""UMLS concept names corresponding to concept_ids""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    umls_cui: Optional[str] = Field(default=None, description="""Primary UMLS Concept Unique Identifier (CUI) for this disease. Key cross-reference for integration with clinical NLP systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    snomed_full_names: Optional[list[str]] = Field(default=None, description="""SNOMED CT preferred full concept names""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    snomed_concept_ids: Optional[list[str]] = Field(default=None, description="""SNOMED CT concept identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    cui_semantic_type: Optional[str] = Field(default=None, description="""UMLS semantic type for the primary CUI (e.g. \"Disease or Syndrome\", \"Neoplastic Process\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    therapeutic_areas: Optional[list[str]] = Field(default=None, description="""Associated therapeutic area classification codes (Open Targets EFO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })


class Drug(PhysicalEntity):
    """
    A drug, compound, or therapeutic agent represented in OptimusKG. Current Neo4j label: `DRG`.

    Property detail from OptimusKG source schema: A pharmacological compound node. Represents 16,766 drugs (8.8% of nodes) including approved drugs, investigational compounds, and biologics. Integrates chemical, regulatory, and clinical metadata from DrugBank, DrugCentral, OnSIDES, and Open Targets. Primary ontologies: ChEMBL, DrugBank, RxNorm. Node file: nodes/drug.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'DRG'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'DRG'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'DrugNode'}},
         'class_uri': 'biolink:Drug',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'description': {'description': 'Free-text description of the '
                                                       "drug's pharmacology, "
                                                       'indications, and mechanism of '
                                                       'action.',
                                        'name': 'description'},
                        'name': {'description': 'Primary drug name (INN or generic '
                                                'name, e.g. "metformin")',
                                 'name': 'name',
                                 'range': 'string'},
                        'source_ids': {'description': 'Source-specific compound '
                                                      'identifiers',
                                       'name': 'source_ids'},
                        'synonyms': {'description': 'Alternative drug names (INNs, '
                                                    'abbreviations, research codes)',
                                     'name': 'synonyms'},
                        'type': {'description': 'Drug type classification (e.g. "Small '
                                                'molecule", "Biologic", "Antibody", '
                                                '"Enzyme", "Oligonucleotide").',
                                 'name': 'type'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Primary drug name (INN or generic name, e.g. \"metformin\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    modulates_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects a drug/intervention/hypothesis to the pathogenic mechanism it modulates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'TherapeuticIntervention', 'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:modulates_pathogenic_mechanism'} })
    targets_gene: Optional[list[str]] = Field(default=None, description="""Connects a drug, intervention, or hypothesis to a target gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'TherapeuticIntervention', 'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:targets_gene'} })
    targets_protein: Optional[list[str]] = Field(default=None, description="""Connects a drug, intervention, or hypothesis to a target protein.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'TherapeuticIntervention', 'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:targets_protein'} })
    type: Optional[str] = Field(default=None, description="""Drug type classification (e.g. \"Small molecule\", \"Biologic\", \"Antibody\", \"Enzyme\", \"Oligonucleotide\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'Phenotype']} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the drug's pharmacology, indications, and mechanism of action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    synonyms: Optional[list[str]] = Field(default=None, description="""Alternative drug names (INNs, abbreviations, research codes)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Drug',
                       'MolecularFunction'],
         'slot_uri': 'skos:altLabel'} })
    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific compound identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    trade_names: Optional[list[str]] = Field(default=None, description="""Commercial brand/trade names (e.g. \"Glucophage\" for metformin)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    accession_numbers: Optional[list[str]] = Field(default=None, description="""Database accession numbers from various sources""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    inchi_key: Optional[str] = Field(default=None, description="""Hashed InChIKey identifier (27-character string). Standard chemical structure fingerprint for deduplication and lookup.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    cd_formula: Optional[str] = Field(default=None, description="""Molecular formula (e.g. \"C10H17N3O6S\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    is_approved: Optional[bool] = Field(default=None, description="""True if the drug is currently approved for clinical use in any jurisdiction""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    has_been_withdrawn: Optional[bool] = Field(default=None, description="""True if the drug has been withdrawn from the market""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    black_box_warning: Optional[bool] = Field(default=None, description="""True if the drug carries an FDA black box (boxed) warning""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    year_of_first_approval: Optional[int] = Field(default=None, description="""Calendar year of first regulatory approval (any jurisdiction)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    maximum_clinical_trial_phase: Optional[float] = Field(default=None, description="""Highest clinical trial phase the drug has reached (0–4). 4 = marketed/approved, 0 = preclinical/experimental.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    status: Optional[str] = Field(default=None, description="""Regulatory development status string (e.g. \"Approved\", \"Investigational\", \"Withdrawn\", \"Experimental\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DatabaseAccession']} })
    chemical_abstracts_service_number: Optional[str] = Field(default=None, description="""CAS Registry Number — the gold-standard chemical compound identifier from the American Chemical Society (e.g. \"57-27-2\" for morphine).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })
    unique_ingredient_identifier: Optional[str] = Field(default=None, description="""FDA Unique Ingredient Identifier (UNII) — a non-proprietary, free, unique, unambiguous, non-semantic, alphanumeric identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug']} })


class Exposure(PhysicalEntity):
    """
    An environmental, chemical, lifestyle, or other exposure concept represented in OptimusKG. Current Neo4j label: `EXP`.

    Property detail from OptimusKG source schema: A chemical, physical, or environmental exposure node. Represents 881 exposures (0.5% of nodes) linked to biological outcomes via CTD (Comparative Toxicogenomics Database). Covers chemical exposures, physical agents, dietary factors, and lifestyle exposures. Source: Comparative Toxicogenomics Database (CTD). Node file: nodes/exposure.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'EXP'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'EXP'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'ExposureNode'}},
         'class_uri': 'biolink:EnvironmentalExposure',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'name': {'description': 'Exposure name (MeSH preferred term, '
                                                'e.g. "Benzo(a)pyrene", "Arsenic")',
                                 'name': 'name',
                                 'range': 'string'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Exposure name (MeSH preferred term, e.g. \"Benzo(a)pyrene\", \"Arsenic\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    source_categories: Optional[list[str]] = Field(default=None, description="""Categories describing the origin or context of the exposure (e.g. \"chemical\", \"biological\", \"physical\", \"dietary\", \"lifestyle\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    source_details: Optional[str] = Field(default=None, description="""Free-text description providing additional source-specific context for the exposure (e.g. specific exposure routes, measurement context)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })


class Gene(PhysicalEntity):
    """
    A gene or gene-level biological entity represented in OptimusKG. Current Neo4j label: `GEN`.

    Property detail from OptimusKG source schema: A protein-coding or non-coding gene node. Represents 61,306 human genes (32.2% of nodes) from Ensembl, harmonized with HGNC approved symbols. Contains rich molecular, functional, pharmacological, and clinical metadata sourced from Open Targets, DisGeNET, Bgee, and HGNC. Primary ontologies: ENSG (Ensembl Gene IDs), NCBIGene. Node file: nodes/gene.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'GEN'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'GEN'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'GeneNode'}},
         'class_uri': 'biolink:Gene',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'name': {'description': 'Full official gene name from HGNC '
                                                '(e.g. "tumor protein p53").',
                                 'name': 'name',
                                 'range': 'string'},
                        'symbol': {'description': 'Official HGNC-approved gene symbol '
                                                  '(e.g. "TP53", "BRCA1"). Primary '
                                                  'human-readable identifier for the '
                                                  'gene.',
                                   'name': 'symbol',
                                   'range': 'string'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Full official gene name from HGNC (e.g. \"tumor protein p53\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    symbol: Optional[str] = Field(default=None, description="""Official HGNC-approved gene symbol (e.g. \"TP53\", \"BRCA1\"). Primary human-readable identifier for the gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    encodes: Optional[list[str]] = Field(default=None, description="""Connects a Gene to a Protein product. Used in the semantic view to normalize gene-associated protein identifiers.""", json_schema_extra = { "linkml_meta": {'domain': 'Gene', 'domain_of': ['Gene'], 'slot_uri': 'RO:0002205'} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    gene_has_expression_context: Optional[str] = Field(default=None, description="""Neo4j relationship `HAS_EXPRESSION_CONTEXT` from `GEN`/Gene to `ECX`/GeneExpressionContext. Links a gene to a reified expression context node capturing direction, molecular subtype, tissue, and provenance.""", json_schema_extra = { "linkml_meta": {'annotations': {'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'ECX'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_EXPRESSION_CONTEXT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'GEN'}},
         'domain': 'Gene',
         'domain_of': ['Gene'],
         'slot_uri': 'okg:has_expression_context'} })
    has_variant: Optional[list[str]] = Field(default=None, description="""Connects a gene to a sequence variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskg:has_variant'} })
    contributes_to_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects a gene, variant, protein, molecular event, or statement to a pathogenic mechanism it contributes to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein', 'MolecularEvent', 'PathogenesisStatement'],
         'slot_uri': 'alskg:contributes_to_pathogenic_mechanism'} })
    has_expression_result: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a differential expression result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'MolecularSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_expression_result'} })
    gene_has_variant: Optional[str] = Field(default=None, description="""Connects a gene to a sequence variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'], 'slot_uri': 'alskg:gene_has_variant'} })
    gene_contributes_to_pathogenic_mechanism: Optional[str] = Field(default=None, description="""Connects a gene to an ALS pathogenic mechanism it contributes to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene'],
         'slot_uri': 'alskg:gene_contributes_to_pathogenic_mechanism'} })
    biotype: Optional[GeneBiotypeEnum] = Field(default=None, description="""Ensembl gene biotype classification (e.g. protein_coding, lncRNA, miRNA). Determines the functional class of the gene product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene']} })


class MolecularFunction(OntologyClass):
    """
    A Gene Ontology molecular function term represented in OptimusKG. Current Neo4j label: `MFN`.

    Property detail from OptimusKG source schema: A Gene Ontology (GO) molecular function node. Represents 10,161 biochemical and enzymatic activities (5.3% of nodes) that gene products perform at the molecular level (e.g. \"protein kinase activity\", \"DNA binding\", \"ATP hydrolysis activity\"). Source: Gene Ontology (GO). Node file: nodes/molecular_function.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'MFN'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'MFN'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'MolecularFunctionNode'}},
         'class_uri': 'biolink:MolecularActivity',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'definition': {'description': 'Formal GO ontology definition '
                                                      'of the molecular function',
                                       'name': 'definition'},
                        'name': {'description': 'GO molecular function name (e.g. '
                                                '"protein kinase activity")',
                                 'name': 'name',
                                 'range': 'string'},
                        'ontology': {'description': 'Source ontology metadata (GO '
                                                    'title, version, license)',
                                     'name': 'ontology'},
                        'synonyms': {'description': 'Alternative GO term names and '
                                                    'synonyms',
                                     'name': 'synonyms'},
                        'xrefs': {'description': 'Cross-references to external '
                                                 'databases',
                                  'name': 'xrefs'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""GO molecular function name (e.g. \"protein kinase activity\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    definition: Optional[str] = Field(default=None, description="""Formal GO ontology definition of the molecular function""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction'],
         'slot_uri': 'IAO:0000115'} })
    synonyms: Optional[list[str]] = Field(default=None, description="""Alternative GO term names and synonyms""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Drug',
                       'MolecularFunction'],
         'slot_uri': 'skos:altLabel'} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    ontology: Optional[str] = Field(default=None, description="""Source ontology metadata (GO title, version, license)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction',
                       'Phenotype']} })


class Phenotype(ClinicalEntity):
    """
    A phenotype or clinical feature represented in OptimusKG. Current Neo4j label: `PHE`.

    Property detail from OptimusKG source schema: A clinical phenotype or phenotypic abnormality node. Represents 19,341 phenotypes (10.2% of nodes) from HPO and MedDRA, describing observable clinical features and traits associated with diseases. Sources: HPO, MedDRA, Open Targets. Node file: nodes/phenotype.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'PHE'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'PHE'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'PhenotypeNode'}},
         'class_uri': 'biolink:PhenotypicFeature',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'ancestors': {'description': 'All transitive ancestor '
                                                     'phenotype term IDs',
                                      'name': 'ancestors'},
                        'broad_synonyms': {'description': 'Broader term synonyms',
                                           'name': 'broad_synonyms'},
                        'children': {'description': 'Direct child phenotype term '
                                                    'identifiers',
                                     'name': 'children'},
                        'code': {'description': 'Primary ontology code for the '
                                                'phenotype term',
                                 'name': 'code'},
                        'concept_ids': {'description': 'UMLS concept IDs linked to '
                                                       'this phenotype',
                                        'name': 'concept_ids'},
                        'concept_names': {'description': 'UMLS concept names '
                                                         'corresponding to concept_ids',
                                          'name': 'concept_names'},
                        'cui_semantic_type': {'description': 'UMLS semantic type for '
                                                             'the primary CUI',
                                              'name': 'cui_semantic_type'},
                        'descendants': {'description': 'All transitive descendant '
                                                       'phenotype term IDs',
                                        'name': 'descendants'},
                        'description': {'description': 'Formal ontology definition of '
                                                       'the phenotype',
                                        'name': 'description'},
                        'exact_synonyms': {'description': 'Exact synonym labels for '
                                                          'this phenotype',
                                           'name': 'exact_synonyms'},
                        'is_leaf': {'description': 'True if this phenotype term has no '
                                                   'children',
                                    'name': 'is_leaf'},
                        'name': {'description': 'Phenotype name (HPO preferred label, '
                                                'e.g. "Seizure", "Intellectual '
                                                'disability")',
                                 'name': 'name',
                                 'range': 'string'},
                        'narrow_synonyms': {'description': 'Narrower term synonyms',
                                            'name': 'narrow_synonyms'},
                        'obsolete_terms': {'description': 'Deprecated phenotype term '
                                                          'labels',
                                           'name': 'obsolete_terms'},
                        'obsolete_xrefs': {'description': 'Deprecated cross-references',
                                           'name': 'obsolete_xrefs'},
                        'ontology': {'description': 'Metadata about the source '
                                                    'ontology (title, version, '
                                                    'license, description)',
                                     'name': 'ontology'},
                        'parents': {'description': 'Direct parent phenotype term '
                                                   'identifiers in the HPO hierarchy',
                                    'name': 'parents'},
                        'related_synonyms': {'description': 'Semantically related '
                                                            'synonym labels',
                                             'name': 'related_synonyms'},
                        'snomed_concept_ids': {'description': 'SNOMED CT concept '
                                                              'identifiers',
                                               'name': 'snomed_concept_ids'},
                        'snomed_full_names': {'description': 'SNOMED CT preferred full '
                                                             'concept names',
                                              'name': 'snomed_full_names'},
                        'type': {'description': 'Phenotype type or ontology '
                                                'classification (e.g. "HPO", "MedDRA '
                                                'LLT", "MedDRA PT").',
                                 'name': 'type'},
                        'umls_cui': {'description': 'Primary UMLS Concept Unique '
                                                    'Identifier for this phenotype',
                                     'name': 'umls_cui'},
                        'xrefs': {'description': 'Cross-references to external '
                                                 'databases (e.g. UMLS, SNOMED, MeSH)',
                                  'name': 'xrefs'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Phenotype name (HPO preferred label, e.g. \"Seizure\", \"Intellectual disability\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    description: Optional[str] = Field(default=None, description="""Formal ontology definition of the phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    code: Optional[str] = Field(default=None, description="""Primary ontology code for the phenotype term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    type: Optional[str] = Field(default=None, description="""Phenotype type or ontology classification (e.g. \"HPO\", \"MedDRA LLT\", \"MedDRA PT\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'Phenotype']} })
    parents: Optional[list[str]] = Field(default=None, description="""Direct parent phenotype term identifiers in the HPO hierarchy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    children: Optional[list[str]] = Field(default=None, description="""Direct child phenotype term identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    ancestors: Optional[list[str]] = Field(default=None, description="""All transitive ancestor phenotype term IDs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    descendants: Optional[list[str]] = Field(default=None, description="""All transitive descendant phenotype term IDs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    is_leaf: Optional[bool] = Field(default=None, description="""True if this phenotype term has no children""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    exact_synonyms: Optional[list[str]] = Field(default=None, description="""Exact synonym labels for this phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    related_synonyms: Optional[list[str]] = Field(default=None, description="""Semantically related synonym labels""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    narrow_synonyms: Optional[list[str]] = Field(default=None, description="""Narrower term synonyms""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    broad_synonyms: Optional[list[str]] = Field(default=None, description="""Broader term synonyms""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    obsolete_terms: Optional[list[str]] = Field(default=None, description="""Deprecated phenotype term labels""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    obsolete_xrefs: Optional[list[str]] = Field(default=None, description="""Deprecated cross-references""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external databases (e.g. UMLS, SNOMED, MeSH)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    concept_ids: Optional[list[str]] = Field(default=None, description="""UMLS concept IDs linked to this phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    concept_names: Optional[list[str]] = Field(default=None, description="""UMLS concept names corresponding to concept_ids""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    umls_cui: Optional[str] = Field(default=None, description="""Primary UMLS Concept Unique Identifier for this phenotype""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    snomed_full_names: Optional[list[str]] = Field(default=None, description="""SNOMED CT preferred full concept names""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    snomed_concept_ids: Optional[list[str]] = Field(default=None, description="""SNOMED CT concept identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    cui_semantic_type: Optional[str] = Field(default=None, description="""UMLS semantic type for the primary CUI""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    ontology: Optional[str] = Field(default=None, description="""Metadata about the source ontology (title, version, license, description)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction',
                       'Phenotype']} })


class Pathway(OntologyClass):
    """
    A biological pathway represented in OptimusKG. Current Neo4j label: `PWY`.

    Property detail from OptimusKG source schema: A biological pathway node. Represents 2,805 curated pathways (1.5% of nodes) from Reactome, covering molecular reactions, signaling cascades, metabolic processes, and disease pathways in human cells. Sources: Open Targets, Reactome. Node file: nodes/pathway.parquet
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'PWY'},
                         'optimus_abbreviation': {'tag': 'optimus_abbreviation',
                                                  'value': 'PWY'},
                         'property_schema_source': {'tag': 'property_schema_source',
                                                    'value': 'PathwayNode'}},
         'class_uri': 'biolink:Pathway',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'name': {'description': 'Reactome pathway name (e.g. '
                                                '"Apoptosis", "Signal Transduction")',
                                 'name': 'name',
                                 'range': 'string'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Reactome pathway name (e.g. \"Apoptosis\", \"Signal Transduction\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    species: Optional[str] = Field(default=None, description="""Species name for the pathway (always \"Homo sapiens\" in OptimusKG, as the pipeline filters to human pathways only)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Pathway']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction'],
         'slot_uri': 'IAO:0000115'} })
    synonyms: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Drug',
                       'MolecularFunction'],
         'slot_uri': 'skos:altLabel'} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    ontology: Optional[str] = Field(default=None, description="""Metadata about the source ontology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction',
                       'Phenotype']} })


class RelationshipAssertion(ConfiguredBaseModel):
    """
    Abstract root class for all typed, asserted relationships between named entities in OptimusKG. All family-level abstract classes and concrete relationship classes inherit subject, object, undirected, sources, and evidence slots from here. Four canonical direct children: HierarchyRelationship, AssociationRelationship, PharmacologicalRelationship, FunctionalAnnotationRelationship. Additional families: ExposureEntityRelationship (under AssociationRelationship), ExpressionRelationship (under AssociationRelationship), MolecularSubtypeRelationship (direct child, covers AnalyticalEntity edges).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'rdf:Statement',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class HierarchyRelationship(RelationshipAssertion):
    """
    A parent, subclass, or ontology hierarchy relationship in the current OptimusKG Neo4j graph. This groups PARENT and IS_A edges while preserving the exact Neo4j relationship type in each concrete subclass.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:HierarchyRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class AssociationRelationship(RelationshipAssertion):
    """
    Abstract family for evidence-bearing association edges between biomedical entities. Covers gene-disease, disease-phenotype, phenotype-gene, drug-drug, drug-gene, exposure-entity, and gene-gene interaction relationships. Renamed from EntityAssociationRelationship (v0.3.0) for clarity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:AssociationRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class FunctionalAnnotationRelationship(RelationshipAssertion):
    """
    Abstract family for GO annotation and pathway membership relationships. Connects genes to biological processes (BPO-GEN), cellular components (CCO-GEN), molecular functions (MFN-GEN), and pathways (PWY-GEN). One of the four canonical relationship families in OptimusKG v0.4.0.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:FunctionalAnnotationRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PharmacologicalRelationship(RelationshipAssertion):
    """
    Abstract family for drug therapeutic-use relationships, including indication, contraindication, off-label use, and adverse drug reactions. Subject is always a Drug node. Renamed from TherapeuticUseRelationship (v0.3.0) to reflect that this family covers all drug action semantics, not only clinical therapeutic use.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:PharmacologicalRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'subject': {'description': 'The source Drug node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ExposureEntityRelationship(AssociationRelationship):
    """
    Abstract family for exposure-to-entity association relationships. Now a subclass of AssociationRelationship rather than a direct child of RelationshipAssertion (v0.4.0 consolidation). Subject is always an Exposure node.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:ExposureEntityRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'subject': {'description': 'The source Exposure node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Exposure'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PhenotypeHierarchyRelationship(HierarchyRelationship):
    """
    Hierarchy relationship between Phenotype nodes, or from a phenotype to a disease when the installed graph uses a PARENT pattern across those labels.

    Property detail: Hierarchical relationships between HPO phenotype terms. Relation: PARENT (is_a, has_part within HPO ontology). Undirected: False. Count: 24,862. Source: HPO.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:PhenotypeHierarchyRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'subject': {'description': 'The source Phenotype node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Phenotype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class MolecularSubtypeRelationship(RelationshipAssertion):
    """
    Abstract family for all relationships involving a MolecularSubtype (AnalyticalEntity) node. Groups disease-to-subtype (HAS_MOLECULAR_SUBTYPE), gene-to-subtype (DYSREGULATED_IN), and subtype-to-anatomy (MEASURED_IN) relationships. Kept as a distinct family because MolecularSubtype is an AnalyticalEntity, not a standard ClinicalEntity, and its relationship semantics differ from standard biomedical association edges.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:MolecularSubtypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class AnatomyGeneExpressionRelationship(AssociationRelationship):
    """
    Parent class for anatomy-to-gene expression relationships, including expression present and expression absent edges.

    Property detail: Gene expression associations between anatomical structures and genes. Relations: EXPRESSION_PRESENT or EXPRESSION_ABSENT. Undirected: True. Count: 8,787,955 (40.3% of all edges). Source: Bgee (curated RNA-seq expression data, v2024-05-17). NOTE: ANA-GEN is the second-largest edge type and the most common category of edges lacking literature support (661/1413 unsupported edges in the PaperQA3 validation), reflecting the lag between data deposition and narrative synthesis in publications.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:AnatomyGeneExpressionRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'The target Gene node for this '
                                                  'relationship family.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'subject': {'description': 'The source Anatomy node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Anatomy'}}})

    expression_rank: Optional[int] = Field(default=None, description="""Bgee expression rank score for this gene in this tissue. Lower rank = higher relative expression. Computed across all tissues.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomyGeneExpressionRelationship']} })
    call_quality: Optional[ExpressionCallQualityEnum] = Field(default=None, description="""Quality level of the Bgee expression call (gold = high confidence, silver = moderate confidence). Based on concordance across evidence types.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomyGeneExpressionRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DiseasePhenotypeRelationship(AssociationRelationship):
    """
    Concrete relationship class for disease-to-phenotype relationships, including phenotype presence annotations.

    Property detail: Clinical associations between diseases and their characteristic phenotypic features. Relation: PHENOTYPE_PRESENT. Undirected: True. Count: 157,144. Source: Open Targets (via HPO annotations).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'okg:DiseasePhenotypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'The target Phenotype node for this '
                                                  'relationship family.',
                                   'name': 'object',
                                   'range': 'Phenotype'},
                        'subject': {'description': 'The source Disease node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Disease'}}})

    aspect: Optional[list[str]] = Field(default=None, description="""HPO annotation aspect categories: \"P\" = Phenotypic abnormality, \"I\" = Mode of inheritance, \"C\" = Onset and clinical course, \"M\" = Clinical modifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    evidence_type: Optional[list[str]] = Field(default=None, description="""Evidence type codes (e.g. \"IEA\" = Inferred from Electronic Annotation, \"PCS\" = Published Clinical Study, \"TAS\" = Traceable Author Statement)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship', 'EvidenceRecord']} })
    frequency: Optional[list[str]] = Field(default=None, description="""Phenotype frequency annotations. May be ontology terms (HP:0040283 = Occasional) or percentage ranges (e.g. \"5-29%\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    onset: Optional[list[str]] = Field(default=None, description="""Age of onset categories (HPO terms, e.g. \"HP:0003577\" = Congenital onset)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    modifiers: Optional[list[str]] = Field(default=None, description="""Clinical modifier HPO terms (e.g. severity, progression)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    sexes: Optional[list[str]] = Field(default=None, description="""Sex-specific occurrence annotations (e.g. \"PATO:0000384\" = male)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    qualifier_not: Optional[bool] = Field(default=None, description="""True if this is an exclusion annotation — the phenotype is explicitly absent/excluded in this disease context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    bio_curation: Optional[list[str]] = Field(default=None, description="""Biocuration provenance strings recording the curator ID and date (e.g. \"ORPHA:orphadata[2023-07-01]\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    references: Optional[list[str]] = Field(default=None, description="""Supporting publication PMIDs or database references (e.g. \"PMID:1234567\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugBiologicalProcessTherapeuticRelationship(PharmacologicalRelationship):
    """
    Concrete relationship class for drug-to-biological-process therapeutic-use relationships.

    Property detail: Drug indications linked to biological processes. Relation: INDICATION. Undirected: True. Count: 62. Source: Open Targets.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'okg:DrugBiologicalProcessTherapeuticRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'highest_clinical_trial_phase': {'description': 'Highest '
                                                                        'clinical '
                                                                        'trial phase '
                                                                        'for this '
                                                                        'drug-process '
                                                                        'indication '
                                                                        '(0-4)',
                                                         'name': 'highest_clinical_trial_phase'},
                        'object': {'description': 'The target BiologicalProcess node '
                                                  'for this relationship family.',
                                   'name': 'object',
                                   'range': 'BiologicalProcess'},
                        'reference_ids': {'description': 'Supporting reference '
                                                         'identifiers',
                                          'name': 'reference_ids'},
                        'subject': {'description': 'The source Drug node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Highest clinical trial phase for this drug-process indication (0-4)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""Supporting reference identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugDiseaseTherapeuticRelationship(PharmacologicalRelationship):
    """
    Parent class for drug-to-disease therapeutic-use relationships, including indication, contraindication, and off-label use.

    Property detail: Drug-disease therapeutic associations including indications, contraindications, and off-label uses. Relations: INDICATION, CONTRAINDICATION, OFF_LABEL_USE. Undirected: True. Count: 70,380. Sources: DrugCentral, Open Targets. Indirect: ATC, Clinical Trials, DailyMed, EMA, FDA, INN, USAN.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:DrugDiseaseTherapeuticRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'drug_disease_id': {'description': 'DrugCentral drug-disease '
                                                           'association identifier',
                                            'name': 'drug_disease_id'},
                        'highest_clinical_trial_phase': {'description': 'Maximum '
                                                                        'clinical '
                                                                        'trial phase '
                                                                        'achieved for '
                                                                        'this '
                                                                        'drug-disease '
                                                                        'pair (0-4). 4 '
                                                                        '= '
                                                                        'approved/marketed '
                                                                        'indication.',
                                                         'name': 'highest_clinical_trial_phase'},
                        'object': {'description': 'The target Disease node for this '
                                                  'relationship family.',
                                   'name': 'object',
                                   'range': 'Disease'},
                        'reference_ids': {'description': 'External reference '
                                                         'identifiers supporting the '
                                                         'association (e.g. '
                                                         'ClinicalTrials.gov IDs, FDA '
                                                         'application numbers)',
                                          'name': 'reference_ids'},
                        'structure_id': {'description': 'DrugCentral internal '
                                                        'structure identifier for the '
                                                        'drug',
                                         'name': 'structure_id'},
                        'subject': {'description': 'The source Drug node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Maximum clinical trial phase achieved for this drug-disease pair (0-4). 4 = approved/marketed indication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral internal structure identifier for the drug""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""External reference identifiers supporting the association (e.g. ClinicalTrials.gov IDs, FDA application numbers)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugPhenotypeTherapeuticRelationship(PharmacologicalRelationship):
    """
    Parent class for drug-to-phenotype therapeutic and adverse-event relationships.

    Property detail: Drug effects on clinical phenotypic outcomes, including adverse reactions, indications, contraindications, and off-label uses. Relations: ADVERSE_DRUG_REACTION, ASSOCIATED_WITH, CONTRAINDICATION, INDICATION, OFF_LABEL_USE. Undirected: True. Count: 13,758. Sources: DrugCentral, OnSIDES, Open Targets. OnSIDES data: adverse drug events extracted from FDA labels using PubMedBERT.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:DrugPhenotypeTherapeuticRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'drug_disease_id': {'description': 'DrugCentral '
                                                           'drug-disease/phenotype '
                                                           'association identifier',
                                            'name': 'drug_disease_id'},
                        'highest_clinical_trial_phase': {'description': 'Highest '
                                                                        'clinical '
                                                                        'trial phase '
                                                                        'for this '
                                                                        'drug-phenotype '
                                                                        'association '
                                                                        '(0-4)',
                                                         'name': 'highest_clinical_trial_phase'},
                        'object': {'description': 'The target Phenotype node for this '
                                                  'relationship family.',
                                   'name': 'object',
                                   'range': 'Phenotype'},
                        'reference_ids': {'description': 'Supporting reference '
                                                         'identifiers',
                                          'name': 'reference_ids'},
                        'structure_id': {'description': 'DrugCentral structure '
                                                        'identifier',
                                         'name': 'structure_id'},
                        'subject': {'description': 'The source Drug node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Highest clinical trial phase for this drug-phenotype association (0-4)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral structure identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease/phenotype association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""Supporting reference identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugDrugRelationship(AssociationRelationship):
    """
    Concrete relationship class for drug-to-drug relationships such as synergistic interaction.

    Property detail: Drug-drug interactions and hierarchical drug relationships. Relations: SYNERGISTIC_INTERACTION, PARENT. Undirected: False. Count: 1,345,376. Source: DrugBank, Open Targets. NOTE: DRG-DRG is the third-largest edge type. It includes both pharmacological interactions (DDIs from DrugBank) and ontological parent-child relationships within drug classification hierarchies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'okg:DrugDrugRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'The target Drug node for this '
                                                  'relationship family.',
                                   'name': 'object',
                                   'range': 'Drug'},
                        'subject': {'description': 'The source Drug node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    interaction_description: Optional[str] = Field(default=None, description="""Free-text description of the drug-drug interaction mechanism, clinical significance, or severity (from DrugBank DDI annotations).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDrugRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugGeneRelationship(AssociationRelationship):
    """
    Parent class for all OptimusKG relationships between Drug and Gene nodes. This groups target, modulation, transporter, enzyme, carrier, and other pharmacologic relationship types.

    Property detail: Drug-target interactions with pharmacological mechanism annotations. Relations: 23 types including ACTIVATOR, AGONIST, ANTAGONIST, INHIBITOR, TARGET, SUBSTRATE, CARRIER, TRANSPORTER, ENZYME, etc. Undirected: False. Count: 20,694. Sources: DrugBank, Open Targets. Indirect: BNF, Clinical Trials, DOI, DailyMed, EMA, Expert, FDA, HMA, ISBN, IUPHAR, KEGG, Other, PMC, Patent, PubChem, PubMed, UniProt, Wikipedia.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:DrugGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'The target Gene node for this '
                                                  'relationship family.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'source_ids': {'description': 'Source-specific interaction '
                                                      'identifiers for '
                                                      'cross-referencing',
                                       'name': 'source_ids'},
                        'subject': {'description': 'The source Drug node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugGeneTargetingRelationship(DrugGeneRelationship):
    """
    Drug-gene relationship indicating target designation, target binding, substrate status, or direct drug-target association.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:DrugGeneTargetingRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'The target Gene node for this '
                                                  'relationship family.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'subject': {'description': 'The source Drug node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugGeneModulationRelationship(DrugGeneRelationship):
    """
    Drug-gene relationship indicating that the drug changes the activity, abundance, state, opening, stability, degradation, release, or function of the gene product.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:DrugGeneModulationRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'The target Gene node for this '
                                                  'relationship family.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'subject': {'description': 'The source Drug node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugGeneRoleRelationship(DrugGeneRelationship):
    """
    Drug-gene relationship describing the role of a gene product in drug metabolism, transport, or carrier behavior.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'okg:DrugGeneRoleRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'The target Gene node for this '
                                                  'relationship family.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'subject': {'description': 'The source Drug node for this '
                                                   'relationship family.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class AnatomyHasParentAnatomyRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:ANA)-[:PARENT]->(:ANA)`, represented with full class names as Anatomy -> Anatomy. Parent-child hierarchy relationship from the source concept to a broader or parent concept in the same or related ontology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'anatomy_parent_anatomy'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'ANA'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PARENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'ANA'}},
         'class_uri': 'okg:AnatomyParentAnatomyRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Anatomy node with Neo4j '
                                                  'label `ANA`.',
                                   'name': 'object',
                                   'range': 'Anatomy'},
                        'original_optimus_relationship_type': {'equals_string': 'PARENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Anatomy node with Neo4j '
                                                   'label `ANA`.',
                                    'name': 'subject',
                                    'range': 'Anatomy'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class AnatomyHasGeneExpressionAbsentRelationship(AnatomyGeneExpressionRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:ANA)-[:EXPRESSION_ABSENT]->(:GEN)`, represented with full class names as Anatomy -> Gene. Gene expression is reported absent in an anatomical context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'anatomy_expression_absent_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'EXPRESSION_ABSENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'ANA'}},
         'class_uri': 'okg:AnatomyExpressionAbsentGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'EXPRESSION_ABSENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Anatomy node with Neo4j '
                                                   'label `ANA`.',
                                    'name': 'subject',
                                    'range': 'Anatomy'}}})

    expression_rank: Optional[int] = Field(default=None, description="""Bgee expression rank score for this gene in this tissue. Lower rank = higher relative expression. Computed across all tissues.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomyGeneExpressionRelationship']} })
    call_quality: Optional[ExpressionCallQualityEnum] = Field(default=None, description="""Quality level of the Bgee expression call (gold = high confidence, silver = moderate confidence). Based on concordance across evidence types.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomyGeneExpressionRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class AnatomyHasGeneExpressionPresentRelationship(AnatomyGeneExpressionRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:ANA)-[:EXPRESSION_PRESENT]->(:GEN)`, represented with full class names as Anatomy -> Gene. Gene expression is reported present in an anatomical context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'anatomy_expression_present_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'EXPRESSION_PRESENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'ANA'}},
         'class_uri': 'okg:AnatomyExpressionPresentGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'EXPRESSION_PRESENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Anatomy node with Neo4j '
                                                   'label `ANA`.',
                                    'name': 'subject',
                                    'range': 'Anatomy'}}})

    expression_rank: Optional[int] = Field(default=None, description="""Bgee expression rank score for this gene in this tissue. Lower rank = higher relative expression. Computed across all tissues.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomyGeneExpressionRelationship']} })
    call_quality: Optional[ExpressionCallQualityEnum] = Field(default=None, description="""Quality level of the Bgee expression call (gold = high confidence, silver = moderate confidence). Based on concordance across evidence types.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomyGeneExpressionRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class BiologicalProcessIsSubclassOfRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:BPO)-[:IS_A]->(:BPO)`, represented with full class names as BiologicalProcess -> BiologicalProcess. Ontology subclass relationship indicating the source concept is a kind of the target concept.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'biologicalprocess_is_a_biologicalprocess'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'BPO'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'IS_A'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'BPO'}},
         'class_uri': 'okg:BiologicalProcessIsABiologicalProcessRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target BiologicalProcess node with '
                                                  'Neo4j label `BPO`.',
                                   'name': 'object',
                                   'range': 'BiologicalProcess'},
                        'original_optimus_relationship_type': {'equals_string': 'IS_A',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source BiologicalProcess node with '
                                                   'Neo4j label `BPO`.',
                                    'name': 'subject',
                                    'range': 'BiologicalProcess'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class BiologicalProcessHasParticipatingGeneRelationship(FunctionalAnnotationRelationship):
    """
    A biological-process-to-gene relationship corresponding to Neo4j `(:BiologicalProcess)-[:INTERACTS_WITH]->(:Gene)`. In the semantic view, interpret as a gene annotated to or participating in a biological process, not necessarily a physical interaction.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'biologicalprocess_interacts_with_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INTERACTS_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'BPO'}},
         'class_uri': 'okg:BiologicalProcessInteractsWithGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'INTERACTS_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source BiologicalProcess node with '
                                                   'Neo4j label `BPO`.',
                                    'name': 'subject',
                                    'range': 'BiologicalProcess'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class CellularComponentIsSubclassOfRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:CCO)-[:IS_A]->(:CCO)`, represented with full class names as CellularComponent -> CellularComponent. Ontology subclass relationship indicating the source concept is a kind of the target concept.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'cellularcomponent_is_a_cellularcomponent'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'CCO'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'IS_A'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'CCO'}},
         'class_uri': 'okg:CellularComponentIsACellularComponentRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target CellularComponent node with '
                                                  'Neo4j label `CCO`.',
                                   'name': 'object',
                                   'range': 'CellularComponent'},
                        'original_optimus_relationship_type': {'equals_string': 'IS_A',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source CellularComponent node with '
                                                   'Neo4j label `CCO`.',
                                    'name': 'subject',
                                    'range': 'CellularComponent'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class CellularComponentHasLocatedGeneRelationship(FunctionalAnnotationRelationship):
    """
    A cellular-component-to-gene relationship corresponding to Neo4j `(:CellularComponent)-[:INTERACTS_WITH]->(:Gene)`. In the semantic view, interpret as gene/gene-product cellular component localization or annotation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'cellularcomponent_interacts_with_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INTERACTS_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'CCO'}},
         'class_uri': 'okg:CellularComponentInteractsWithGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'INTERACTS_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source CellularComponent node with '
                                                   'Neo4j label `CCO`.',
                                    'name': 'subject',
                                    'range': 'CellularComponent'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DiseaseHasParentDiseaseRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DIS)-[:PARENT]->(:DIS)`, represented with full class names as Disease -> Disease. Parent-child hierarchy relationship from the source concept to a broader or parent concept in the same or related ontology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'disease_parent_disease'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'DIS'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PARENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DIS'}},
         'class_uri': 'okg:DiseaseParentDiseaseRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Disease node with Neo4j '
                                                  'label `DIS`.',
                                   'name': 'object',
                                   'range': 'Disease'},
                        'original_optimus_relationship_type': {'equals_string': 'PARENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Disease node with Neo4j '
                                                   'label `DIS`.',
                                    'name': 'subject',
                                    'range': 'Disease'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DiseaseAssociatedWithGeneRelationship(AssociationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DIS)-[:ASSOCIATED_WITH]->(:GEN)`, represented with full class names as Disease -> Gene. Association relationship; generally evidence-bearing but not necessarily causal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'disease_associated_with_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ASSOCIATED_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DIS'}},
         'class_uri': 'okg:DiseaseAssociatedWithGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'ASSOCIATED_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Disease node with Neo4j '
                                                   'label `DIS`.',
                                    'name': 'subject',
                                    'range': 'Disease'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DiseaseHasPhenotypeRelationship(DiseasePhenotypeRelationship):
    """
    A disease-to-phenotype relationship corresponding to Neo4j `(:Disease)-[:PHENOTYPE_PRESENT]->(:Phenotype)`. It means the disease has/presents the phenotype. The inverse natural-language reading is \"the phenotype is present in the disease\", but the current graph direction is Disease -> Phenotype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'disease_phenotype_present_phenotype'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'PHE'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PHENOTYPE_PRESENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DIS'}},
         'class_uri': 'okg:DiseasePhenotypePresentPhenotypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Phenotype node with Neo4j '
                                                  'label `PHE`.',
                                   'name': 'object',
                                   'range': 'Phenotype'},
                        'original_optimus_relationship_type': {'equals_string': 'PHENOTYPE_PRESENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Disease node with Neo4j '
                                                   'label `DIS`.',
                                    'name': 'subject',
                                    'range': 'Disease'}}})

    aspect: Optional[list[str]] = Field(default=None, description="""HPO annotation aspect categories: \"P\" = Phenotypic abnormality, \"I\" = Mode of inheritance, \"C\" = Onset and clinical course, \"M\" = Clinical modifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    evidence_type: Optional[list[str]] = Field(default=None, description="""Evidence type codes (e.g. \"IEA\" = Inferred from Electronic Annotation, \"PCS\" = Published Clinical Study, \"TAS\" = Traceable Author Statement)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship', 'EvidenceRecord']} })
    frequency: Optional[list[str]] = Field(default=None, description="""Phenotype frequency annotations. May be ontology terms (HP:0040283 = Occasional) or percentage ranges (e.g. \"5-29%\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    onset: Optional[list[str]] = Field(default=None, description="""Age of onset categories (HPO terms, e.g. \"HP:0003577\" = Congenital onset)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    modifiers: Optional[list[str]] = Field(default=None, description="""Clinical modifier HPO terms (e.g. severity, progression)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    sexes: Optional[list[str]] = Field(default=None, description="""Sex-specific occurrence annotations (e.g. \"PATO:0000384\" = male)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    qualifier_not: Optional[bool] = Field(default=None, description="""True if this is an exclusion annotation — the phenotype is explicitly absent/excluded in this disease context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    bio_curation: Optional[list[str]] = Field(default=None, description="""Biocuration provenance strings recording the curator ID and date (e.g. \"ORPHA:orphadata[2023-07-01]\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    references: Optional[list[str]] = Field(default=None, description="""Supporting publication PMIDs or database references (e.g. \"PMID:1234567\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugHasIndicationForBiologicalProcessRelationship(DrugBiologicalProcessTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INDICATION]->(:BPO)`, represented with full class names as Drug -> BiologicalProcess. Drug has an indicated therapeutic use for a disease, phenotype, or biological process context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_indication_biologicalprocess'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'BPO'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INDICATION'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugIndicationBiologicalProcessRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target BiologicalProcess node with '
                                                  'Neo4j label `BPO`.',
                                   'name': 'object',
                                   'range': 'BiologicalProcess'},
                        'original_optimus_relationship_type': {'equals_string': 'INDICATION',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Highest clinical trial phase for this drug-process indication (0-4)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""Supporting reference identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugContraindicatedForDiseaseRelationship(DrugDiseaseTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:CONTRAINDICATION]->(:DIS)`, represented with full class names as Drug -> Disease. Drug is contraindicated for a disease or phenotype context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_contraindication_disease'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'DIS'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'CONTRAINDICATION'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugContraindicationDiseaseRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Disease node with Neo4j '
                                                  'label `DIS`.',
                                   'name': 'object',
                                   'range': 'Disease'},
                        'original_optimus_relationship_type': {'equals_string': 'CONTRAINDICATION',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Maximum clinical trial phase achieved for this drug-disease pair (0-4). 4 = approved/marketed indication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral internal structure identifier for the drug""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""External reference identifiers supporting the association (e.g. ClinicalTrials.gov IDs, FDA application numbers)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugIndicatedForDiseaseRelationship(DrugDiseaseTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INDICATION]->(:DIS)`, represented with full class names as Drug -> Disease. Drug has an indicated therapeutic use for a disease, phenotype, or biological process context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_indication_disease'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'DIS'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INDICATION'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugIndicationDiseaseRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Disease node with Neo4j '
                                                  'label `DIS`.',
                                   'name': 'object',
                                   'range': 'Disease'},
                        'original_optimus_relationship_type': {'equals_string': 'INDICATION',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Maximum clinical trial phase achieved for this drug-disease pair (0-4). 4 = approved/marketed indication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral internal structure identifier for the drug""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""External reference identifiers supporting the association (e.g. ClinicalTrials.gov IDs, FDA application numbers)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugUsedOffLabelForDiseaseRelationship(DrugDiseaseTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:OFF_LABEL_USE]->(:DIS)`, represented with full class names as Drug -> Disease. Drug has off-label use for a disease or phenotype context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_off_label_use_disease'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'DIS'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'OFF_LABEL_USE'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugOffLabelUseDiseaseRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Disease node with Neo4j '
                                                  'label `DIS`.',
                                   'name': 'object',
                                   'range': 'Disease'},
                        'original_optimus_relationship_type': {'equals_string': 'OFF_LABEL_USE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Maximum clinical trial phase achieved for this drug-disease pair (0-4). 4 = approved/marketed indication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral internal structure identifier for the drug""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""External reference identifiers supporting the association (e.g. ClinicalTrials.gov IDs, FDA application numbers)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugHasParentDrugRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:PARENT]->(:DRG)`, represented with full class names as Drug -> Drug. Parent-child hierarchy relationship from the source concept to a broader or parent concept in the same or related ontology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_parent_drug'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'DRG'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PARENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugParentDrugRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Drug node with Neo4j label '
                                                  '`DRG`.',
                                   'name': 'object',
                                   'range': 'Drug'},
                        'original_optimus_relationship_type': {'equals_string': 'PARENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugHasSynergisticInteractionWithDrugRelationship(DrugDrugRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:SYNERGISTIC_INTERACTION]->(:DRG)`, represented with full class names as Drug -> Drug. Drug-drug relationship indicating synergistic interaction.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_synergistic_interaction_drug'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'DRG'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'SYNERGISTIC_INTERACTION'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugSynergisticInteractionDrugRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Drug node with Neo4j label '
                                                  '`DRG`.',
                                   'name': 'object',
                                   'range': 'Drug'},
                        'original_optimus_relationship_type': {'equals_string': 'SYNERGISTIC_INTERACTION',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    interaction_description: Optional[str] = Field(default=None, description="""Free-text description of the drug-drug interaction mechanism, clinical significance, or severity (from DrugBank DDI annotations).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDrugRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugActivatesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ACTIVATOR]->(:GEN)`, represented with full class names as Drug -> Gene. Drug activates the gene product or target associated with the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_activator_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ACTIVATOR'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugActivatorGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'ACTIVATOR',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugAgonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:AGONIST]->(:GEN)`, represented with full class names as Drug -> Gene. Drug acts as an agonist of the gene product or target associated with the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_agonist_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'AGONIST'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugAgonistGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'AGONIST',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugAllostericAntagonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ALLOSTERIC_ANTAGONIST]->(:GEN)`, represented with full class names as Drug -> Gene. Drug acts as an allosteric antagonist of the gene product or target associated with the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_allosteric_antagonist_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ALLOSTERIC_ANTAGONIST'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugAllostericAntagonistGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'ALLOSTERIC_ANTAGONIST',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugAntagonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ANTAGONIST]->(:GEN)`, represented with full class names as Drug -> Gene. Drug acts as an antagonist of the gene product or target associated with the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_antagonist_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ANTAGONIST'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugAntagonistGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'ANTAGONIST',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugBindsGeneProductRelationship(DrugGeneTargetingRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:BINDING_AGENT]->(:GEN)`, represented with full class names as Drug -> Gene. Drug binds the gene product or target associated with the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_binding_agent_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'BINDING_AGENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugBindingAgentGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'BINDING_AGENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugBlocksGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:BLOCKER]->(:GEN)`, represented with full class names as Drug -> Gene. Drug blocks the gene product or target associated with the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_blocker_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'BLOCKER'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugBlockerGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'BLOCKER',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugHasCarrierGeneProductRelationship(DrugGeneRoleRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:CARRIER]->(:GEN)`, represented with full class names as Drug -> Gene. Drug-gene relationship where the gene product is a carrier in pharmacologic context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_carrier_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'CARRIER'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugCarrierGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'CARRIER',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugDegradesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:DEGRADER]->(:GEN)`, represented with full class names as Drug -> Gene. Drug degrades or induces degradation of the gene product or target.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_degrader_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'DEGRADER'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugDegraderGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'DEGRADER',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugHasMetabolizingEnzymeGeneProductRelationship(DrugGeneRoleRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ENZYME]->(:GEN)`, represented with full class names as Drug -> Gene. Drug-gene relationship where the gene product is an enzyme in drug metabolism or action context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_enzyme_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ENZYME'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugEnzymeGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'ENZYME',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugInhibitsGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INHIBITOR]->(:GEN)`, represented with full class names as Drug -> Gene. Drug inhibits the gene product or target associated with the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_inhibitor_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INHIBITOR'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugInhibitorGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'INHIBITOR',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugInverseAgonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INVERSE_AGONIST]->(:GEN)`, represented with full class names as Drug -> Gene. Drug acts as an inverse agonist of the gene product or target.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_inverse_agonist_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INVERSE_AGONIST'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugInverseAgonistGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'INVERSE_AGONIST',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugModulatesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:MODULATOR]->(:GEN)`, represented with full class names as Drug -> Gene. Drug modulates the gene product or target associated with the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_modulator_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'MODULATOR'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugModulatorGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'MODULATOR',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugNegativeAllostericModulatorOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:NEGATIVE_ALLOSTERIC_MODULATOR]->(:GEN)`, represented with full class names as Drug -> Gene. Drug acts as a negative allosteric modulator of the gene product or target.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_negative_allosteric_modulator_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'NEGATIVE_ALLOSTERIC_MODULATOR'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugNegativeAllostericModulatorGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'NEGATIVE_ALLOSTERIC_MODULATOR',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugNegativelyModulatesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:NEGATIVE_MODULATOR]->(:GEN)`, represented with full class names as Drug -> Gene. Drug negatively modulates the gene product or target.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_negative_modulator_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'NEGATIVE_MODULATOR'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugNegativeModulatorGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'NEGATIVE_MODULATOR',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugOpensGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:OPENER]->(:GEN)`, represented with full class names as Drug -> Gene. Drug opens the gene product or target, often a channel target.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_opener_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'OPENER'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugOpenerGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'OPENER',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugPartialAgonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:PARTIAL_AGONIST]->(:GEN)`, represented with full class names as Drug -> Gene. Drug acts as a partial agonist of the gene product or target.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_partial_agonist_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PARTIAL_AGONIST'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugPartialAgonistGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'PARTIAL_AGONIST',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugPositiveAllostericModulatorOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:POSITIVE_ALLOSTERIC_MODULATOR]->(:GEN)`, represented with full class names as Drug -> Gene. Drug acts as a positive allosteric modulator of the gene product or target.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_positive_allosteric_modulator_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'POSITIVE_ALLOSTERIC_MODULATOR'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugPositiveAllostericModulatorGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'POSITIVE_ALLOSTERIC_MODULATOR',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugPositivelyModulatesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:POSITIVE_MODULATOR]->(:GEN)`, represented with full class names as Drug -> Gene. Drug positively modulates the gene product or target.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_positive_modulator_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'POSITIVE_MODULATOR'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugPositiveModulatorGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'POSITIVE_MODULATOR',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugReleasingAgentOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:RELEASING_AGENT]->(:GEN)`, represented with full class names as Drug -> Gene. Drug acts as a releasing agent affecting the gene product or related target system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_releasing_agent_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'RELEASING_AGENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugReleasingAgentGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'RELEASING_AGENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugStabilizesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:STABILISER]->(:GEN)`, represented with full class names as Drug -> Gene. Drug stabilizes the gene product or target.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_stabiliser_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'STABILISER'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugStabiliserGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'STABILISER',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugIsSubstrateOfGeneProductRelationship(DrugGeneTargetingRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:SUBSTRATE]->(:GEN)`, represented with full class names as Drug -> Gene. Drug is a substrate of the gene product, often an enzyme or transporter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_substrate_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'SUBSTRATE'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugSubstrateGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'SUBSTRATE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugTargetsGeneProductRelationship(DrugGeneTargetingRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:TARGET]->(:GEN)`, represented with full class names as Drug -> Gene. Drug targets the gene product associated with the gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_target_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'TARGET'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugTargetGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'TARGET',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugHasTransporterGeneProductRelationship(DrugGeneRoleRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:TRANSPORTER]->(:GEN)`, represented with full class names as Drug -> Gene. Drug-gene relationship where the gene product is a transporter in pharmacologic context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_transporter_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'TRANSPORTER'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugTransporterGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'TRANSPORTER',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    source_ids: Optional[list[str]] = Field(default=None, description="""Source-specific interaction identifiers for cross-referencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DrugGeneRelationship']} })
    mechanisms_of_action: Optional[list[str]] = Field(default=None, description="""Free-text descriptions of the biochemical or pharmacological mechanism of action for this drug-gene interaction (e.g. \"Competitive inhibitor\", \"Irreversible inhibitor\", \"Partial agonist\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    source_urls: Optional[list[str]] = Field(default=None, description="""URLs linking to supporting evidence records in source databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugGeneRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugHasAdversePhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ADVERSE_DRUG_REACTION]->(:PHE)`, represented with full class names as Drug -> Phenotype. Drug-to-phenotype relationship indicating an adverse drug reaction.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_adverse_drug_reaction_phenotype'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'PHE'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ADVERSE_DRUG_REACTION'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugAdverseDrugReactionPhenotypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Phenotype node with Neo4j '
                                                  'label `PHE`.',
                                   'name': 'object',
                                   'range': 'Phenotype'},
                        'original_optimus_relationship_type': {'equals_string': 'ADVERSE_DRUG_REACTION',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Highest clinical trial phase for this drug-phenotype association (0-4)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral structure identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease/phenotype association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""Supporting reference identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugAssociatedWithPhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ASSOCIATED_WITH]->(:PHE)`, represented with full class names as Drug -> Phenotype. Association relationship; generally evidence-bearing but not necessarily causal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_associated_with_phenotype'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'PHE'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ASSOCIATED_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugAssociatedWithPhenotypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Phenotype node with Neo4j '
                                                  'label `PHE`.',
                                   'name': 'object',
                                   'range': 'Phenotype'},
                        'original_optimus_relationship_type': {'equals_string': 'ASSOCIATED_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Highest clinical trial phase for this drug-phenotype association (0-4)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral structure identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease/phenotype association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""Supporting reference identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugContraindicatedForPhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:CONTRAINDICATION]->(:PHE)`, represented with full class names as Drug -> Phenotype. Drug is contraindicated for a disease or phenotype context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_contraindication_phenotype'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'PHE'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'CONTRAINDICATION'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugContraindicationPhenotypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Phenotype node with Neo4j '
                                                  'label `PHE`.',
                                   'name': 'object',
                                   'range': 'Phenotype'},
                        'original_optimus_relationship_type': {'equals_string': 'CONTRAINDICATION',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Highest clinical trial phase for this drug-phenotype association (0-4)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral structure identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease/phenotype association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""Supporting reference identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugIndicatedForPhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INDICATION]->(:PHE)`, represented with full class names as Drug -> Phenotype. Drug has an indicated therapeutic use for a disease, phenotype, or biological process context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_indication_phenotype'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'PHE'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INDICATION'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugIndicationPhenotypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Phenotype node with Neo4j '
                                                  'label `PHE`.',
                                   'name': 'object',
                                   'range': 'Phenotype'},
                        'original_optimus_relationship_type': {'equals_string': 'INDICATION',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Highest clinical trial phase for this drug-phenotype association (0-4)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral structure identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease/phenotype association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""Supporting reference identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugUsedOffLabelForPhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:OFF_LABEL_USE]->(:PHE)`, represented with full class names as Drug -> Phenotype. Drug has off-label use for a disease or phenotype context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_off_label_use_phenotype'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'PHE'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'OFF_LABEL_USE'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DRG'}},
         'class_uri': 'okg:DrugOffLabelUsePhenotypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Phenotype node with Neo4j '
                                                  'label `PHE`.',
                                   'name': 'object',
                                   'range': 'Phenotype'},
                        'original_optimus_relationship_type': {'equals_string': 'OFF_LABEL_USE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Drug node with Neo4j label '
                                                   '`DRG`.',
                                    'name': 'subject',
                                    'range': 'Drug'}}})

    highest_clinical_trial_phase: Optional[float] = Field(default=None, description="""Highest clinical trial phase for this drug-phenotype association (0-4)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    structure_id: Optional[str] = Field(default=None, description="""DrugCentral structure identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    drug_disease_id: Optional[str] = Field(default=None, description="""DrugCentral drug-disease/phenotype association identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    reference_ids: Optional[list[str]] = Field(default=None, description="""Supporting reference identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugBiologicalProcessTherapeuticRelationship',
                       'DrugDiseaseTherapeuticRelationship',
                       'DrugPhenotypeTherapeuticRelationship']} })
    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ExposureAssociatedWithBiologicalProcessRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:INTERACTS_WITH]->(:BPO)`, represented with full class names as Exposure -> BiologicalProcess. Generic interaction or annotation-style relationship. Interpret according to the source and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'exposure_interacts_with_biologicalprocess'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'BPO'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INTERACTS_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'EXP'}},
         'class_uri': 'okg:ExposureInteractsWithBiologicalProcessRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target BiologicalProcess node with '
                                                  'Neo4j label `BPO`.',
                                   'name': 'object',
                                   'range': 'BiologicalProcess'},
                        'original_optimus_relationship_type': {'equals_string': 'INTERACTS_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Exposure node with Neo4j '
                                                   'label `EXP`.',
                                    'name': 'subject',
                                    'range': 'Exposure'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ExposureAssociatedWithCellularComponentRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:INTERACTS_WITH]->(:CCO)`, represented with full class names as Exposure -> CellularComponent. Generic interaction or annotation-style relationship. Interpret according to the source and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'exposure_interacts_with_cellularcomponent'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'CCO'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INTERACTS_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'EXP'}},
         'class_uri': 'okg:ExposureInteractsWithCellularComponentRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target CellularComponent node with '
                                                  'Neo4j label `CCO`.',
                                   'name': 'object',
                                   'range': 'CellularComponent'},
                        'original_optimus_relationship_type': {'equals_string': 'INTERACTS_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Exposure node with Neo4j '
                                                   'label `EXP`.',
                                    'name': 'subject',
                                    'range': 'Exposure'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ExposureLinkedToDiseaseRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:LINKED_TO]->(:DIS)`, represented with full class names as Exposure -> Disease. Generic linkage relation; interpret as associative rather than causal unless source evidence says otherwise.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'exposure_linked_to_disease'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'DIS'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'LINKED_TO'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'EXP'}},
         'class_uri': 'okg:ExposureLinkedToDiseaseRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Disease node with Neo4j '
                                                  'label `DIS`.',
                                   'name': 'object',
                                   'range': 'Disease'},
                        'original_optimus_relationship_type': {'equals_string': 'LINKED_TO',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Exposure node with Neo4j '
                                                   'label `EXP`.',
                                    'name': 'subject',
                                    'range': 'Exposure'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ExposureHasParentExposureRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:PARENT]->(:EXP)`, represented with full class names as Exposure -> Exposure. Parent-child hierarchy relationship from the source concept to a broader or parent concept in the same or related ontology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'exposure_parent_exposure'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'EXP'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PARENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'EXP'}},
         'class_uri': 'okg:ExposureParentExposureRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Exposure node with Neo4j '
                                                  'label `EXP`.',
                                   'name': 'object',
                                   'range': 'Exposure'},
                        'original_optimus_relationship_type': {'equals_string': 'PARENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Exposure node with Neo4j '
                                                   'label `EXP`.',
                                    'name': 'subject',
                                    'range': 'Exposure'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ExposureAssociatedWithGeneRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:INTERACTS_WITH]->(:GEN)`, represented with full class names as Exposure -> Gene. Generic interaction or annotation-style relationship. Interpret according to the source and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'exposure_interacts_with_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INTERACTS_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'EXP'}},
         'class_uri': 'okg:ExposureInteractsWithGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'INTERACTS_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Exposure node with Neo4j '
                                                   'label `EXP`.',
                                    'name': 'subject',
                                    'range': 'Exposure'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ExposureAssociatedWithMolecularFunctionRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:INTERACTS_WITH]->(:MFN)`, represented with full class names as Exposure -> MolecularFunction. Generic interaction or annotation-style relationship. Interpret according to the source and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'exposure_interacts_with_molecularfunction'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'MFN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INTERACTS_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'EXP'}},
         'class_uri': 'okg:ExposureInteractsWithMolecularFunctionRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target MolecularFunction node with '
                                                  'Neo4j label `MFN`.',
                                   'name': 'object',
                                   'range': 'MolecularFunction'},
                        'original_optimus_relationship_type': {'equals_string': 'INTERACTS_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Exposure node with Neo4j '
                                                   'label `EXP`.',
                                    'name': 'subject',
                                    'range': 'Exposure'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class GeneInteractsWithGeneRelationship(AssociationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:GEN)-[:INTERACTS_WITH]->(:GEN)`, represented with full class names as Gene -> Gene. Generic interaction or annotation-style relationship. Interpret according to the source and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'gene_interacts_with_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INTERACTS_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'GEN'}},
         'class_uri': 'okg:GeneInteractsWithGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'INTERACTS_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Gene node with Neo4j label '
                                                   '`GEN`.',
                                    'name': 'subject',
                                    'range': 'Gene'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class MolecularFunctionEnabledByGeneRelationship(FunctionalAnnotationRelationship):
    """
    A molecular-function-to-gene relationship corresponding to Neo4j `(:MolecularFunction)-[:INTERACTS_WITH]->(:Gene)`. In the semantic view, interpret as the gene/gene product enabling or being annotated to the molecular function.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'molecularfunction_interacts_with_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INTERACTS_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'MFN'}},
         'class_uri': 'okg:MolecularFunctionInteractsWithGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'INTERACTS_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source MolecularFunction node with '
                                                   'Neo4j label `MFN`.',
                                    'name': 'subject',
                                    'range': 'MolecularFunction'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class MolecularFunctionIsSubclassOfRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:MFN)-[:IS_A]->(:MFN)`, represented with full class names as MolecularFunction -> MolecularFunction. Ontology subclass relationship indicating the source concept is a kind of the target concept.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'molecularfunction_is_a_molecularfunction'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'MFN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'IS_A'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'MFN'}},
         'class_uri': 'okg:MolecularFunctionIsAMolecularFunctionRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target MolecularFunction node with '
                                                  'Neo4j label `MFN`.',
                                   'name': 'object',
                                   'range': 'MolecularFunction'},
                        'original_optimus_relationship_type': {'equals_string': 'IS_A',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source MolecularFunction node with '
                                                   'Neo4j label `MFN`.',
                                    'name': 'subject',
                                    'range': 'MolecularFunction'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PhenotypeHasParentDiseaseRelationship(PhenotypeHierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:PHE)-[:PARENT]->(:DIS)`, represented with full class names as Phenotype -> Disease. Parent-child hierarchy relationship from the source concept to a broader or parent concept in the same or related ontology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'phenotype_parent_disease'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'DIS'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PARENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'PHE'}},
         'class_uri': 'okg:PhenotypeParentDiseaseRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Disease node with Neo4j '
                                                  'label `DIS`.',
                                   'name': 'object',
                                   'range': 'Disease'},
                        'original_optimus_relationship_type': {'equals_string': 'PARENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Phenotype node with Neo4j '
                                                   'label `PHE`.',
                                    'name': 'subject',
                                    'range': 'Phenotype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PhenotypeAssociatedWithGeneRelationship(AssociationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:PHE)-[:ASSOCIATED_WITH]->(:GEN)`, represented with full class names as Phenotype -> Gene. Association relationship; generally evidence-bearing but not necessarily causal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'phenotype_associated_with_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ASSOCIATED_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'PHE'}},
         'class_uri': 'okg:PhenotypeAssociatedWithGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'ASSOCIATED_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Phenotype node with Neo4j '
                                                   'label `PHE`.',
                                    'name': 'subject',
                                    'range': 'Phenotype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PhenotypeHasParentPhenotypeRelationship(PhenotypeHierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:PHE)-[:PARENT]->(:PHE)`, represented with full class names as Phenotype -> Phenotype. Parent-child hierarchy relationship from the source concept to a broader or parent concept in the same or related ontology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'phenotype_parent_phenotype'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'PHE'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PARENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'PHE'}},
         'class_uri': 'okg:PhenotypeParentPhenotypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Phenotype node with Neo4j '
                                                  'label `PHE`.',
                                   'name': 'object',
                                   'range': 'Phenotype'},
                        'original_optimus_relationship_type': {'equals_string': 'PARENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Phenotype node with Neo4j '
                                                   'label `PHE`.',
                                    'name': 'subject',
                                    'range': 'Phenotype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PathwayHasMemberGeneRelationship(FunctionalAnnotationRelationship):
    """
    A pathway-to-gene relationship corresponding to Neo4j `(:Pathway)-[:INTERACTS_WITH]->(:Gene)`. In the semantic view, interpret as pathway membership/participation rather than a generic interaction.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'pathway_interacts_with_gene'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'GEN'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INTERACTS_WITH'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'PWY'}},
         'class_uri': 'okg:PathwayInteractsWithGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Gene node with Neo4j label '
                                                  '`GEN`.',
                                   'name': 'object',
                                   'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'INTERACTS_WITH',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Pathway node with Neo4j '
                                                   'label `PWY`.',
                                    'name': 'subject',
                                    'range': 'Pathway'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PathwayHasParentPathwayRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:PWY)-[:PARENT]->(:PWY)`, represented with full class names as Pathway -> Pathway. Parent-child hierarchy relationship from the source concept to a broader or parent concept in the same or related ontology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'pathway_parent_pathway'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'PWY'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PARENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'PWY'}},
         'class_uri': 'okg:PathwayParentPathwayRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Pathway node with Neo4j '
                                                  'label `PWY`.',
                                   'name': 'object',
                                   'range': 'Pathway'},
                        'original_optimus_relationship_type': {'equals_string': 'PARENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Pathway node with Neo4j '
                                                   'label `PWY`.',
                                    'name': 'subject',
                                    'range': 'Pathway'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DiseaseHasMolecularSubtypeConcreteRelationship(MolecularSubtypeRelationship):
    """
    Reified schema class for the Neo4j pattern `(:DIS)-[:HAS_MOLECULAR_SUBTYPE]->(:MST)`, represented with full class names as Disease -> MolecularSubtype. Indicates that a disease node is associated with a transcriptome-derived molecular subtype. This is a cross-cutting classification relationship, not an ontological subclass assertion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'disease_has_molecular_subtype'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'MST'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_MOLECULAR_SUBTYPE'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DIS'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'Cross-cutting classification '
                                                         'relationship; does not imply '
                                                         'ontological subclassing. A '
                                                         'Disease can '
                                                         'HAS_MOLECULAR_SUBTYPE '
                                                         'multiple MolecularSubtype '
                                                         'nodes simultaneously.'}},
         'class_uri': 'okg:DiseaseHasMolecularSubtypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target MolecularSubtype node with '
                                                  'Neo4j label `MST`.',
                                   'name': 'object',
                                   'range': 'MolecularSubtype'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_MOLECULAR_SUBTYPE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Disease node with Neo4j '
                                                   'label `DIS`.',
                                    'name': 'subject',
                                    'range': 'Disease'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class MolecularSubtypeHasParentDiseaseRelationship(HierarchyRelationship):
    """
    Reified schema class for the Neo4j pattern `(:MST)-[:PARENT]->(:DIS)`, represented with full class names as MolecularSubtype -> Disease. Anchors a molecular subtype node to its parent disease in the knowledge graph hierarchy. Reuses the existing PARENT relationship type for compatibility with disease DAG traversal patterns.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'molecular_subtype_has_parent_disease'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'DIS'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PARENT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'MST'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'Reuses PARENT relationship '
                                                         'type for MST->DIS edges; '
                                                         'semantically means the '
                                                         'molecular subtype is grouped '
                                                         'under its anchor disease '
                                                         'node in the hierarchy.'}},
         'class_uri': 'okg:MolecularSubtypeParentDiseaseRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Disease node with Neo4j '
                                                  'label `DIS`.',
                                   'name': 'object',
                                   'range': 'Disease'},
                        'original_optimus_relationship_type': {'equals_string': 'PARENT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source MolecularSubtype node with '
                                                   'Neo4j label `MST`.',
                                    'name': 'subject',
                                    'range': 'MolecularSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class MolecularSubtypeMeasuredInAnatomyRelationship(MolecularSubtypeRelationship):
    """
    Reified schema class for the Neo4j pattern `(:MST)-[:MEASURED_IN]->(:ANA)`, represented with full class names as MolecularSubtype -> Anatomy. Indicates the tissue context in which a molecular subtype was characterized (e.g. motor cortex, spinal cord). ALS-TE is cortex-only in the current NYGC dataset; ALS-Ox and ALS-Glia have both cortex and cord characterizations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'molecular_subtype_measured_in_anatomy'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'ANA'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'MEASURED_IN'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'MST'}},
         'class_uri': 'okg:MolecularSubtypeMeasuredInAnatomyRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Anatomy node with Neo4j '
                                                  'label `ANA`.',
                                   'name': 'object',
                                   'range': 'Anatomy'},
                        'original_optimus_relationship_type': {'equals_string': 'MEASURED_IN',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source MolecularSubtype node with '
                                                   'Neo4j label `MST`.',
                                    'name': 'subject',
                                    'range': 'MolecularSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ProvenanceEntity(ConfiguredBaseModel):
    """
    Abstract root for schema infrastructure and provenance records. Subclasses document the origin, identity, and evidence lineage of graph content without themselves being biomedical knowledge entities. Replaces the former SemanticEntity grouping for non-entity classes. Children: DataSource, Publication, DatabaseAccession (+ CrossReference), Synonym.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'prov:Entity',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    pass


class Sources(ConfiguredBaseModel):
    """
    Provenance tracking struct present on every node and edge in OptimusKG. Distinguishes between datasets that directly contributed the entity (primary ingestors) and those referenced indirectly through aggregators. Example direct sources: Open Targets, DisGeNET, Bgee. Example indirect sources: ClinGen, PsyGeNET, UniProt (via Open Targets).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'source_schema': {'tag': 'source_schema',
                                           'value': 'optimuskg_schema.yaml'}},
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    direct: Optional[list[str]] = Field(default=None, description="""List of primary data source names that directly contributed this entity or relationship to OptimusKG (e.g. \"Open Targets\", \"DisGeNET\", \"Bgee\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sources']} })
    indirect: Optional[list[str]] = Field(default=None, description="""List of upstream data sources referenced via provenance of primary sources (e.g. \"ClinGen\", \"PsyGeNET\", \"UniProt\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sources']} })


class OntologyMetadata(ConfiguredBaseModel):
    """
    Metadata about the source ontology for a node. Captured verbatim from the OWL or JSON ontology file header at ingestion time.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'source_schema': {'tag': 'source_schema',
                                           'value': 'optimuskg_schema.yaml'}},
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""Human-readable title of the ontology (e.g. \"Human Phenotype Ontology\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyMetadata']} })
    description: Optional[str] = Field(default=None, description="""Brief textual description of the ontology's scope and purpose""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph']} })
    license: Optional[str] = Field(default=None, description="""License under which the ontology is distributed (e.g. \"CC BY 4.0\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyMetadata']} })
    version: Optional[str] = Field(default=None, description="""Version string or release date of the ontology (e.g. \"v2025-05-06\" for HPO, \"v656\" for DOID, \"current\" for dynamic releases)""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyMetadata', 'DatabaseAccession']} })


class Protein(PhysicalEntity):
    """
    A protein or protein-level biological entity associated with or encoded by a Gene. This semantic-view class normalizes values that may appear in OptimusKG gene properties such as associated_proteins.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Protein',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    has_database_accession: Optional[list[str]] = Field(default=None, description="""Connects a semantic entity to a database-specific accession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein', 'ProteinIsoform'],
         'slot_uri': 'alskg:has_database_accession'} })
    has_isoform: Optional[list[str]] = Field(default=None, description="""Connects a Protein to a more specific ProteinIsoform.""", json_schema_extra = { "linkml_meta": {'domain': 'Protein', 'domain_of': ['Protein'], 'slot_uri': 'alskg:has_isoform'} })
    contributes_to_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects a gene, variant, protein, molecular event, or statement to a pathogenic mechanism it contributes to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein', 'MolecularEvent', 'PathogenesisStatement'],
         'slot_uri': 'alskg:contributes_to_pathogenic_mechanism'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class ProteinIsoform(Protein):
    """
    A specific protein isoform or translated product, for example an Ensembl protein accession that may represent a transcript-specific protein product.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskg:ProteinIsoform',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    has_database_accession: Optional[list[str]] = Field(default=None, description="""Connects a semantic entity to a database-specific accession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protein', 'ProteinIsoform'],
         'slot_uri': 'alskg:has_database_accession'} })
    has_isoform: Optional[list[str]] = Field(default=None, description="""Connects a Protein to a more specific ProteinIsoform.""", json_schema_extra = { "linkml_meta": {'domain': 'Protein', 'domain_of': ['Protein'], 'slot_uri': 'alskg:has_isoform'} })
    contributes_to_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects a gene, variant, protein, molecular event, or statement to a pathogenic mechanism it contributes to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein', 'MolecularEvent', 'PathogenesisStatement'],
         'slot_uri': 'alskg:contributes_to_pathogenic_mechanism'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class DatabaseAccession(ProvenanceEntity):
    """
    A database-specific identifier or accession for a biological entity. This class allows accessions to be modeled as nodes rather than JSON strings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskg:DatabaseAccession',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    accession: Optional[str] = Field(default=None, description="""The local accession string within a source database, for example P40261 or ENSP00000299964.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession'], 'slot_uri': 'alskg:accession'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    version: Optional[str] = Field(default=None, description="""Version of an accession, database record, dataset, or schema when known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyMetadata', 'DatabaseAccession'],
         'slot_uri': 'pav:version'} })
    status: Optional[str] = Field(default=None, description="""Status of a record, accession, drug, or assertion, such as reviewed, unreviewed, approved, withdrawn, active, or obsolete.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DatabaseAccession'], 'slot_uri': 'alskg:status'} })


class DataSource(ProvenanceEntity):
    """
    A database, data resource, or source vocabulary contributing identifiers, evidence, or assertions to OptimusKG.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    source_type: Optional[str] = Field(default=None, description="""Type of source, for example ontology, database, literature corpus, aggregator, or computed dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSource'], 'slot_uri': 'alskg:source_type'} })
    url: Optional[str] = Field(default=None, description="""A resolvable URL for a source, publication, evidence record, or web resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSource', 'Publication', 'ExternalKnowledgeReference'],
         'slot_uri': 'schema:url'} })


class Publication(ProvenanceEntity):
    """
    A publication or bibliographic reference that supports an OptimusKG assertion or evidence item.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Publication',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    pmid: Optional[str] = Field(default=None, description="""PubMed identifier for a publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication'], 'slot_uri': 'biolink:pmid'} })
    doi: Optional[str] = Field(default=None, description="""Digital Object Identifier for a publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Publication'], 'slot_uri': 'biolink:doi'} })
    url: Optional[str] = Field(default=None, description="""A resolvable URL for a source, publication, evidence record, or web resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSource', 'Publication', 'ExternalKnowledgeReference'],
         'slot_uri': 'schema:url'} })


class EvidenceRecord(ConfiguredBaseModel):
    """
    A structured evidence item supporting a node, relationship, or knowledge statement in the semantic view.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:EvidenceType',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    evidence_type: Optional[str] = Field(default=None, description="""Evidence category, evidence code, or source-specific evidence type supporting an assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseasePhenotypeRelationship', 'EvidenceRecord'],
         'slot_uri': 'biolink:has_evidence'} })
    confidence_score: Optional[float] = Field(default=None, description="""Numeric confidence score for an assertion or result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'EvidenceStatement'],
         'slot_uri': 'alskg:confidence_score'} })
    has_publication: Optional[list[str]] = Field(default=None, description="""Connects an evidence record or statement to a supporting publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'Study', 'Dataset', 'ClinicalTrial'],
         'slot_uri': 'biolink:publications'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })


class Synonym(ProvenanceEntity):
    """
    A lexical synonym, alias, obsolete label, or alternate name with optional source attribution.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'skos:altLabel',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    synonym_scope: Optional[str] = Field(default=None, description="""Scope or type of synonym, such as exact, broad, narrow, related, symbol synonym, obsolete symbol, or trade name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synonym'], 'slot_uri': 'alskg:synonym_scope'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class CrossReference(DatabaseAccession):
    """
    A cross-reference from an OptimusKG entity to an external database or ontology identifier.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Attribute',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    accession: Optional[str] = Field(default=None, description="""The local accession string within a source database, for example P40261 or ENSP00000299964.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession'], 'slot_uri': 'alskg:accession'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    version: Optional[str] = Field(default=None, description="""Version of an accession, database record, dataset, or schema when known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyMetadata', 'DatabaseAccession'],
         'slot_uri': 'pav:version'} })
    status: Optional[str] = Field(default=None, description="""Status of a record, accession, drug, or assertion, such as reviewed, unreviewed, approved, withdrawn, active, or obsolete.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'DatabaseAccession'], 'slot_uri': 'alskg:status'} })


class GeneHasExpressionContextRelationship(RelationshipAssertion):
    """
    Reified schema class for the Neo4j pattern `(:GEN)-[:HAS_EXPRESSION_CONTEXT]->(:GeneExpressionContext)`. Links a gene to a context node recording direction, molecular subtype, tissue, and provenance of a differential expression finding.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'gene_has_expression_context'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'ECX'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_EXPRESSION_CONTEXT'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'GEN'}},
         'class_uri': 'okg:GeneHasExpressionContextRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target GeneExpressionContext node '
                                                  'with Neo4j label `ECX`.',
                                   'name': 'object',
                                   'range': 'GeneExpressionContext'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_EXPRESSION_CONTEXT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source Gene node with Neo4j label '
                                                   '`GEN`.',
                                    'name': 'subject',
                                    'range': 'Gene'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ExpressionContextInAnatomyRelationship(RelationshipAssertion):
    """
    Reified schema class for the Neo4j pattern `(:ECX)-[:IN_ANATOMY]->(:ANA)`. Links a GeneExpressionContext node to the tissue in which the differential expression was measured. Not present for iPSC cell model contexts without a corresponding anatomy node.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'expression_context_in_anatomy'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'ANA'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'IN_ANATOMY'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'ECX'}},
         'class_uri': 'okg:ExpressionContextInAnatomyRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target Anatomy node with Neo4j '
                                                  'label `ANA`.',
                                   'name': 'object',
                                   'range': 'Anatomy'},
                        'original_optimus_relationship_type': {'equals_string': 'IN_ANATOMY',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source GeneExpressionContext node '
                                                   'with Neo4j label `ECX`.',
                                    'name': 'subject',
                                    'range': 'GeneExpressionContext'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ExpressionContextInMolecularSubtypeRelationship(RelationshipAssertion):
    """
    Reified schema class for the Neo4j pattern `(:ECX)-[:HAS_MOLECULAR_SUBTYPE]->(:MST)`. Links a GeneExpressionContext node to the molecular subtype whose transcriptomic signature the gene contributes to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'expression_context_in_molecular_subtype'},
                         'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'MST'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_MOLECULAR_SUBTYPE'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'ECX'}},
         'class_uri': 'okg:ExpressionContextInMolecularSubtypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'description': 'Target MolecularSubtype node with '
                                                  'Neo4j label `MST`.',
                                   'name': 'object',
                                   'range': 'MolecularSubtype'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_MOLECULAR_SUBTYPE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'description': 'Source GeneExpressionContext node '
                                                   'with Neo4j label `ECX`.',
                                    'name': 'subject',
                                    'range': 'GeneExpressionContext'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class AmyotrophicLateralSclerosis(Disease):
    """
    Amyotrophic lateral sclerosis as the focal disease class for ALS-KG. Use this class for the ALS disease node when extending OptimusKG; it may be represented by the same MONDO/DOID identifier used by the OptimusKG Disease node.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'ALS'}},
         'class_uri': 'MONDO:0004976',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Primary disease name (preferred label in the source ontology)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    has_als_subtype: Optional[list[str]] = Field(default=None, description="""Connects ALS disease to an ALS subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'AmyotrophicLateralSclerosis'],
         'slot_uri': 'alskg:has_subtype'} })
    has_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects ALS, an ALS subtype, or an assertion to a pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_pathogenic_mechanism'} })
    has_phenotype_observation: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_phenotype_observation'} })
    affects_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or result to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'RO:0002131'} })
    involves_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or observation to a relevant cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'alskg:involves_cell_type'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    disease_has_molecular_subtype: Optional[str] = Field(default=None, description="""Current OptimusKG Neo4j relationship `HAS_MOLECULAR_SUBTYPE` from `DIS`/Disease to `MST`/MolecularSubtype. Indicates that a disease node is associated with a transcriptome-derived molecular subtype. Orthogonal to the ontological disease hierarchy; represents a classification layer derived from unsupervised multi-omic clustering.""", json_schema_extra = { "linkml_meta": {'annotations': {'neo4j_end_label': {'tag': 'neo4j_end_label', 'value': 'MST'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_MOLECULAR_SUBTYPE'},
                         'neo4j_start_label': {'tag': 'neo4j_start_label',
                                               'value': 'DIS'}},
         'domain': 'Disease',
         'domain_of': ['Disease'],
         'slot_uri': 'okg:has_molecular_subtype'} })
    disease_has_als_subtype: Optional[str] = Field(default=None, description="""Disease-to-subtype relationship meaning the disease has the ALS subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease'], 'slot_uri': 'alskg:disease_has_als_subtype'} })
    description: Optional[str] = Field(default=None, description="""Free-text disease description from the ontology definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    code: Optional[str] = Field(default=None, description="""Primary ontology code / identifier for the disease term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    parents: Optional[list[str]] = Field(default=None, description="""Direct parent disease term identifiers in the ontology hierarchy. Enables traversal of the disease DAG (directed acyclic graph).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    children: Optional[list[str]] = Field(default=None, description="""Direct child disease term identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    ancestors: Optional[list[str]] = Field(default=None, description="""All transitive ancestor (parent-of-parent-of-...) disease term IDs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    descendants: Optional[list[str]] = Field(default=None, description="""All transitive descendant (child-of-child-of-...) disease term IDs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    is_leaf: Optional[bool] = Field(default=None, description="""True if this disease term has no children (leaf node in ontology tree)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    exact_synonyms: Optional[list[str]] = Field(default=None, description="""Exact lexical synonyms (same meaning, different spelling/abbreviation)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    related_synonyms: Optional[list[str]] = Field(default=None, description="""Semantically related synonyms (close but not exact meaning)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    narrow_synonyms: Optional[list[str]] = Field(default=None, description="""Narrower term synonyms (more specific concepts)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    broad_synonyms: Optional[list[str]] = Field(default=None, description="""Broader term synonyms (more general concepts)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    obsolete_terms: Optional[list[str]] = Field(default=None, description="""Deprecated or retired disease term labels""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    obsolete_xrefs: Optional[list[str]] = Field(default=None, description="""Deprecated cross-references to external databases""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external databases (e.g. ICD-10, OMIM, MeSH, MedDRA). Formatted as CURIE strings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    concept_ids: Optional[list[str]] = Field(default=None, description="""UMLS concept IDs (CUIs) linked to this disease""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    concept_names: Optional[list[str]] = Field(default=None, description="""UMLS concept names corresponding to concept_ids""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    umls_cui: Optional[str] = Field(default=None, description="""Primary UMLS Concept Unique Identifier (CUI) for this disease. Key cross-reference for integration with clinical NLP systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    snomed_full_names: Optional[list[str]] = Field(default=None, description="""SNOMED CT preferred full concept names""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    snomed_concept_ids: Optional[list[str]] = Field(default=None, description="""SNOMED CT concept identifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    cui_semantic_type: Optional[str] = Field(default=None, description="""UMLS semantic type for the primary CUI (e.g. \"Disease or Syndrome\", \"Neoplastic Process\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease', 'Phenotype']} })
    therapeutic_areas: Optional[list[str]] = Field(default=None, description="""Associated therapeutic area classification codes (Open Targets EFO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease']} })


class DiseaseSubtype(ClinicalEntity):
    """
    Abstract class for a subtype of a disease, including clinical, genetic, molecular, pathology, and progression-based subtypes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'alskg:DiseaseSubtype',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    is_subtype_of: Optional[str] = Field(default=None, description="""Connects an ALS subtype to the disease it subtypes, usually amyotrophic lateral sclerosis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:is_subtype_of'} })
    has_subtype_scheme: Optional[list[str]] = Field(default=None, description="""Connects a subtype to the scheme under which it is defined or assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_scheme'} })
    has_subtype_criterion: Optional[list[str]] = Field(default=None, description="""Connects a subtype to a criterion used to define or assign it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_criterion'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class ALSSubtype(DiseaseSubtype):
    """
    An ALS subtype defined by clinical onset, genotype, molecular signature, pathology, progression rate, anatomy, cell type, or another explicit subtype criterion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'AST'}},
         'class_uri': 'alskg:ALSSubtype',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    is_subtype_of: Optional[str] = Field(default=None, description="""Connects an ALS subtype to the disease it subtypes, usually amyotrophic lateral sclerosis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:is_subtype_of'} })
    has_subtype_scheme: Optional[list[str]] = Field(default=None, description="""Connects a subtype to the scheme under which it is defined or assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_scheme'} })
    has_subtype_criterion: Optional[list[str]] = Field(default=None, description="""Connects a subtype to a criterion used to define or assign it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_criterion'} })
    is_defined_by_gene: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_gene'} })
    is_defined_by_variant: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_variant'} })
    is_defined_by_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:is_defined_by_pathogenic_mechanism'} })
    has_phenotype_observation: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_phenotype_observation'} })
    affects_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or result to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'RO:0002131'} })
    involves_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or observation to a relevant cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'alskg:involves_cell_type'} })
    has_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects ALS, an ALS subtype, or an assertion to a pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_pathogenic_mechanism'} })
    has_expression_result: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a differential expression result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'MolecularSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_expression_result'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    als_subtype_is_subtype_of_disease: Optional[str] = Field(default=None, description="""Subtype-to-disease relationship meaning the ALS subtype is a subtype of the disease.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_is_subtype_of_disease'} })
    als_subtype_has_subtype_scheme: Optional[str] = Field(default=None, description="""Connects an ALS subtype to its subtype scheme or taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_scheme'} })
    als_subtype_has_subtype_criterion: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or assignment criterion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_criterion'} })
    als_subtype_defined_by_gene: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_defined_by_gene'} })
    als_subtype_defined_by_variant: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_defined_by_variant'} })
    als_subtype_has_pathogenic_mechanism: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a pathogenic mechanism implicated in that subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_pathogenic_mechanism'} })
    als_subtype_affects_anatomy: Optional[str] = Field(default=None, description="""Connects an ALS subtype to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_affects_anatomy'} })
    als_subtype_involves_cell_type: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a relevant or affected cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_involves_cell_type'} })
    als_subtype_has_phenotype_observation: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_phenotype_observation'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class MolecularSubtype(ALSSubtype):
    """
    A molecular ALS subtype defined by transcriptomic, multi-omic, pathology-associated, or computational evidence. This class preserves compatibility with the current Neo4j `MST` label while making MolecularSubtype a proper subclass of ALSSubtype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'neo4j_label': {'tag': 'neo4j_label', 'value': 'MST'}},
         'class_uri': 'alskg:MolecularSubtype',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'name': {'description': 'Short molecular subtype name (e.g. '
                                                '"ALS-Ox", "ALS-Glia", "ALS-TE")',
                                 'name': 'name',
                                 'range': 'string'},
                        'original_optimus_label': {'equals_string': 'MST',
                                                   'name': 'original_optimus_label'}}})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Short molecular subtype name (e.g. \"ALS-Ox\", \"ALS-Glia\", \"ALS-TE\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[Literal["MST"]] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype'],
         'equals_string': 'MST'} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    has_subtype_scheme: Optional[list[str]] = Field(default=None, description="""Connects a subtype to the scheme under which it is defined or assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_scheme'} })
    has_subtype_criterion: Optional[list[str]] = Field(default=None, description="""Connects a subtype to a criterion used to define or assign it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_criterion'} })
    has_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects ALS, an ALS subtype, or an assertion to a pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_pathogenic_mechanism'} })
    affects_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or result to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'RO:0002131'} })
    involves_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or observation to a relevant cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'alskg:involves_cell_type'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    has_phenotype_observation: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_phenotype_observation'} })
    has_expression_result: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a differential expression result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'MolecularSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_expression_result'} })
    full_name: Optional[str] = Field(default=None, description="""Full descriptive name of the molecular subtype (e.g. \"ALS Oxidative Stress / Mitochondrial Dysfunction subtype\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    defining_mechanism: Optional[str] = Field(default=None, description="""Primary biological mechanism or pathway that defines this subtype (e.g. \"Oxidative phosphorylation dysregulation and proteotoxic stress\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    key_pathways: Optional[list[str]] = Field(default=None, description="""Key biological pathways or gene sets enriched in this subtype (e.g. \"Interferon-alpha signaling\", \"Oxidative phosphorylation\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    classification_basis: Optional[MolecularSubtypeClassificationBasisEnum] = Field(default=None, description="""Computational basis used to define and assign membership in this subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    tissue_origin: Optional[list[str]] = Field(default=None, description="""Tissues or biological contexts in which this subtype was characterized (e.g. \"motor cortex\", \"spinal cord\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    prevalence_pct: Optional[float] = Field(default=None, description="""Estimated prevalence of this subtype as a percentage of ALS patient postmortem samples in the defining cohort.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    survival_months_median: Optional[float] = Field(default=None, description="""Median patient survival in months from symptom onset to death for this molecular subtype, where available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    onset_age_mean: Optional[float] = Field(default=None, description="""Mean age of disease onset (years) for patients assigned to this molecular subtype, where available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    prognosis_note: Optional[str] = Field(default=None, description="""Free-text summary of prognostic differences associated with this molecular subtype relative to others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    cohort: Optional[str] = Field(default=None, description="""Patient cohort in which this subtype was defined (e.g. \"NYGC_ALS_Consortium_postmortem_cortex\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    pubmed_id: Optional[str] = Field(default=None, description="""PubMed identifier of the primary publication defining this molecular subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    label_color: Optional[str] = Field(default=None, description="""Display color used in the original publication's visualizations (e.g. \"blue\" for ALS-Ox, \"gold\" for ALS-Glia, \"red\" for ALS-TE). Informational only.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype']} })
    is_subtype_of: Optional[str] = Field(default=None, description="""Connects an ALS subtype to the disease it subtypes, usually amyotrophic lateral sclerosis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:is_subtype_of'} })
    is_defined_by_gene: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_gene'} })
    is_defined_by_variant: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_variant'} })
    is_defined_by_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:is_defined_by_pathogenic_mechanism'} })
    als_subtype_is_subtype_of_disease: Optional[str] = Field(default=None, description="""Subtype-to-disease relationship meaning the ALS subtype is a subtype of the disease.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_is_subtype_of_disease'} })
    als_subtype_has_subtype_scheme: Optional[str] = Field(default=None, description="""Connects an ALS subtype to its subtype scheme or taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_scheme'} })
    als_subtype_has_subtype_criterion: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or assignment criterion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_criterion'} })
    als_subtype_defined_by_gene: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_defined_by_gene'} })
    als_subtype_defined_by_variant: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_defined_by_variant'} })
    als_subtype_has_pathogenic_mechanism: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a pathogenic mechanism implicated in that subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_pathogenic_mechanism'} })
    als_subtype_affects_anatomy: Optional[str] = Field(default=None, description="""Connects an ALS subtype to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_affects_anatomy'} })
    als_subtype_involves_cell_type: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a relevant or affected cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_involves_cell_type'} })
    als_subtype_has_phenotype_observation: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_phenotype_observation'} })


class ClinicalSubtype(ALSSubtype):
    """
    ALS subtype defined primarily by clinical presentation, such as bulbar-onset ALS, limb-onset ALS, ALS-FTD, upper-motor-neuron-predominant ALS, or lower-motor-neuron-predominant ALS.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'CST'}},
         'class_uri': 'alskg:ClinicalSubtype',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    is_subtype_of: Optional[str] = Field(default=None, description="""Connects an ALS subtype to the disease it subtypes, usually amyotrophic lateral sclerosis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:is_subtype_of'} })
    has_subtype_scheme: Optional[list[str]] = Field(default=None, description="""Connects a subtype to the scheme under which it is defined or assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_scheme'} })
    has_subtype_criterion: Optional[list[str]] = Field(default=None, description="""Connects a subtype to a criterion used to define or assign it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_criterion'} })
    is_defined_by_gene: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_gene'} })
    is_defined_by_variant: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_variant'} })
    is_defined_by_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:is_defined_by_pathogenic_mechanism'} })
    has_phenotype_observation: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_phenotype_observation'} })
    affects_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or result to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'RO:0002131'} })
    involves_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or observation to a relevant cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'alskg:involves_cell_type'} })
    has_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects ALS, an ALS subtype, or an assertion to a pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_pathogenic_mechanism'} })
    has_expression_result: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a differential expression result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'MolecularSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_expression_result'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    als_subtype_is_subtype_of_disease: Optional[str] = Field(default=None, description="""Subtype-to-disease relationship meaning the ALS subtype is a subtype of the disease.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_is_subtype_of_disease'} })
    als_subtype_has_subtype_scheme: Optional[str] = Field(default=None, description="""Connects an ALS subtype to its subtype scheme or taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_scheme'} })
    als_subtype_has_subtype_criterion: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or assignment criterion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_criterion'} })
    als_subtype_defined_by_gene: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_defined_by_gene'} })
    als_subtype_defined_by_variant: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_defined_by_variant'} })
    als_subtype_has_pathogenic_mechanism: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a pathogenic mechanism implicated in that subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_pathogenic_mechanism'} })
    als_subtype_affects_anatomy: Optional[str] = Field(default=None, description="""Connects an ALS subtype to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_affects_anatomy'} })
    als_subtype_involves_cell_type: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a relevant or affected cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_involves_cell_type'} })
    als_subtype_has_phenotype_observation: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_phenotype_observation'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class GeneticSubtype(ALSSubtype):
    """
    ALS subtype defined by a causal, risk-associated, or clinically meaningful gene/variant, such as SOD1-ALS, C9orf72-ALS, TARDBP-ALS, or FUS-ALS.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'GST'}},
         'class_uri': 'alskg:GeneticSubtype',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    is_subtype_of: Optional[str] = Field(default=None, description="""Connects an ALS subtype to the disease it subtypes, usually amyotrophic lateral sclerosis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:is_subtype_of'} })
    has_subtype_scheme: Optional[list[str]] = Field(default=None, description="""Connects a subtype to the scheme under which it is defined or assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_scheme'} })
    has_subtype_criterion: Optional[list[str]] = Field(default=None, description="""Connects a subtype to a criterion used to define or assign it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_criterion'} })
    is_defined_by_gene: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_gene'} })
    is_defined_by_variant: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_variant'} })
    is_defined_by_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:is_defined_by_pathogenic_mechanism'} })
    has_phenotype_observation: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_phenotype_observation'} })
    affects_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or result to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'RO:0002131'} })
    involves_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or observation to a relevant cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'alskg:involves_cell_type'} })
    has_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects ALS, an ALS subtype, or an assertion to a pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_pathogenic_mechanism'} })
    has_expression_result: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a differential expression result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'MolecularSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_expression_result'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    als_subtype_is_subtype_of_disease: Optional[str] = Field(default=None, description="""Subtype-to-disease relationship meaning the ALS subtype is a subtype of the disease.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_is_subtype_of_disease'} })
    als_subtype_has_subtype_scheme: Optional[str] = Field(default=None, description="""Connects an ALS subtype to its subtype scheme or taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_scheme'} })
    als_subtype_has_subtype_criterion: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or assignment criterion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_criterion'} })
    als_subtype_defined_by_gene: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_defined_by_gene'} })
    als_subtype_defined_by_variant: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_defined_by_variant'} })
    als_subtype_has_pathogenic_mechanism: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a pathogenic mechanism implicated in that subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_pathogenic_mechanism'} })
    als_subtype_affects_anatomy: Optional[str] = Field(default=None, description="""Connects an ALS subtype to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_affects_anatomy'} })
    als_subtype_involves_cell_type: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a relevant or affected cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_involves_cell_type'} })
    als_subtype_has_phenotype_observation: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_phenotype_observation'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class PathologySubtype(ALSSubtype):
    """
    ALS subtype defined by pathology or proteinopathy pattern, such as TDP-43 pathology or SOD1 aggregation pattern.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'PST'}},
         'class_uri': 'alskg:PathologySubtype',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    is_subtype_of: Optional[str] = Field(default=None, description="""Connects an ALS subtype to the disease it subtypes, usually amyotrophic lateral sclerosis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:is_subtype_of'} })
    has_subtype_scheme: Optional[list[str]] = Field(default=None, description="""Connects a subtype to the scheme under which it is defined or assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_scheme'} })
    has_subtype_criterion: Optional[list[str]] = Field(default=None, description="""Connects a subtype to a criterion used to define or assign it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_criterion'} })
    is_defined_by_gene: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_gene'} })
    is_defined_by_variant: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_variant'} })
    is_defined_by_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:is_defined_by_pathogenic_mechanism'} })
    has_phenotype_observation: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_phenotype_observation'} })
    affects_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or result to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'RO:0002131'} })
    involves_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or observation to a relevant cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'alskg:involves_cell_type'} })
    has_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects ALS, an ALS subtype, or an assertion to a pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_pathogenic_mechanism'} })
    has_expression_result: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a differential expression result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'MolecularSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_expression_result'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    als_subtype_is_subtype_of_disease: Optional[str] = Field(default=None, description="""Subtype-to-disease relationship meaning the ALS subtype is a subtype of the disease.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_is_subtype_of_disease'} })
    als_subtype_has_subtype_scheme: Optional[str] = Field(default=None, description="""Connects an ALS subtype to its subtype scheme or taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_scheme'} })
    als_subtype_has_subtype_criterion: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or assignment criterion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_criterion'} })
    als_subtype_defined_by_gene: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_defined_by_gene'} })
    als_subtype_defined_by_variant: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_defined_by_variant'} })
    als_subtype_has_pathogenic_mechanism: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a pathogenic mechanism implicated in that subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_pathogenic_mechanism'} })
    als_subtype_affects_anatomy: Optional[str] = Field(default=None, description="""Connects an ALS subtype to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_affects_anatomy'} })
    als_subtype_involves_cell_type: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a relevant or affected cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_involves_cell_type'} })
    als_subtype_has_phenotype_observation: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_phenotype_observation'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class ProgressionSubtype(ALSSubtype):
    """
    ALS subtype defined by disease progression trajectory, such as fast-progressor, slow-progressor, or respiratory-onset progression pattern.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'PGS'}},
         'class_uri': 'alskg:ProgressionSubtype',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    is_subtype_of: Optional[str] = Field(default=None, description="""Connects an ALS subtype to the disease it subtypes, usually amyotrophic lateral sclerosis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:is_subtype_of'} })
    has_subtype_scheme: Optional[list[str]] = Field(default=None, description="""Connects a subtype to the scheme under which it is defined or assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_scheme'} })
    has_subtype_criterion: Optional[list[str]] = Field(default=None, description="""Connects a subtype to a criterion used to define or assign it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSubtype', 'DiseaseSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_subtype_criterion'} })
    is_defined_by_gene: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_gene'} })
    is_defined_by_variant: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:is_defined_by_variant'} })
    is_defined_by_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects an ALS subtype to a defining pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:is_defined_by_pathogenic_mechanism'} })
    has_phenotype_observation: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_phenotype_observation'} })
    affects_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or result to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'RO:0002131'} })
    involves_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or observation to a relevant cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'alskg:involves_cell_type'} })
    has_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects ALS, an ALS subtype, or an assertion to a pathogenic mechanism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype'],
         'slot_uri': 'alskg:has_pathogenic_mechanism'} })
    has_expression_result: Optional[list[str]] = Field(default=None, description="""Connects a disease or subtype to a differential expression result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'MolecularSubtype', 'ALSSubtype'],
         'slot_uri': 'alskg:has_expression_result'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    als_subtype_is_subtype_of_disease: Optional[str] = Field(default=None, description="""Subtype-to-disease relationship meaning the ALS subtype is a subtype of the disease.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_is_subtype_of_disease'} })
    als_subtype_has_subtype_scheme: Optional[str] = Field(default=None, description="""Connects an ALS subtype to its subtype scheme or taxonomy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_scheme'} })
    als_subtype_has_subtype_criterion: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or assignment criterion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_subtype_criterion'} })
    als_subtype_defined_by_gene: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_defined_by_gene'} })
    als_subtype_defined_by_variant: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a defining or characteristic variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_defined_by_variant'} })
    als_subtype_has_pathogenic_mechanism: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a pathogenic mechanism implicated in that subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_pathogenic_mechanism'} })
    als_subtype_affects_anatomy: Optional[str] = Field(default=None, description="""Connects an ALS subtype to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'], 'slot_uri': 'alskg:als_subtype_affects_anatomy'} })
    als_subtype_involves_cell_type: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a relevant or affected cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_involves_cell_type'} })
    als_subtype_has_phenotype_observation: Optional[str] = Field(default=None, description="""Connects an ALS subtype to a contextual phenotype observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ALSSubtype'],
         'slot_uri': 'alskg:als_subtype_has_phenotype_observation'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class SubtypeScheme(AnalyticalEntity):
    """
    A scheme or taxonomy used to classify ALS subtypes, such as clinical-onset subtype, ALS-OPM motor phenotype, genotype subtype, molecular cluster, pathology subtype, or progression subtype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'SSC'}},
         'class_uri': 'alskg:SubtypeScheme',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class SubtypeCriterion(AnalyticalEntity):
    """
    A criterion used to assign or define an ALS subtype, such as a gene variant, symptom pattern, anatomical onset region, transcriptomic signature, pathology feature, or progression threshold.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'SCR'}},
         'class_uri': 'alskg:SubtypeCriterion',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class SequenceVariant(PhysicalEntity):
    """
    A genomic sequence variant relevant to ALS, including SNVs, indels, structural variants, copy number changes, and repeat expansions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'VAR'}},
         'class_uri': 'SO:0001060',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    has_variant_type: Optional[str] = Field(default=None, description="""Type of sequence variant, preferably represented with a Sequence Ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'SO:0001060'} })
    has_pathogenicity: Optional[PathogenicityEnum] = Field(default=None, description="""Clinical or biological pathogenicity classification of a variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'alskg:has_pathogenicity'} })
    affects_gene: Optional[list[str]] = Field(default=None, description="""Connects a sequence variant to a gene it affects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'RO:0004020'} })
    alters_protein: Optional[list[str]] = Field(default=None, description="""Connects a sequence variant to a protein or protein product it alters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'alskg:alters_protein'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    variant_affects_gene: Optional[str] = Field(default=None, description="""Connects a sequence variant to the gene it affects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'alskg:variant_affects_gene'} })
    variant_alters_protein: Optional[str] = Field(default=None, description="""Connects a sequence variant to a protein it alters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'alskg:variant_alters_protein'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class RepeatExpansion(SequenceVariant):
    """
    A repeat expansion variant, such as the C9orf72 hexanucleotide repeat expansion associated with ALS/FTD.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'REX'}},
         'class_uri': 'SO:0002165',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    has_variant_type: Optional[str] = Field(default=None, description="""Type of sequence variant, preferably represented with a Sequence Ontology term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'SO:0001060'} })
    has_pathogenicity: Optional[PathogenicityEnum] = Field(default=None, description="""Clinical or biological pathogenicity classification of a variant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'alskg:has_pathogenicity'} })
    affects_gene: Optional[list[str]] = Field(default=None, description="""Connects a sequence variant to a gene it affects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'RO:0004020'} })
    alters_protein: Optional[list[str]] = Field(default=None, description="""Connects a sequence variant to a protein or protein product it alters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'alskg:alters_protein'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    variant_affects_gene: Optional[str] = Field(default=None, description="""Connects a sequence variant to the gene it affects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'alskg:variant_affects_gene'} })
    variant_alters_protein: Optional[str] = Field(default=None, description="""Connects a sequence variant to a protein it alters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SequenceVariant'], 'slot_uri': 'alskg:variant_alters_protein'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class CellType(OntologyClass):
    """
    A cell type relevant to ALS biology, such as upper motor neuron, lower motor neuron, astrocyte, microglia, oligodendrocyte, skeletal muscle cell, or immune cell. Prefer Cell Ontology CURIEs when available.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'CLT'}},
         'class_uri': 'biolink:Cell',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    definition: Optional[str] = Field(default=None, description="""Formal textual definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction'],
         'slot_uri': 'IAO:0000115'} })
    synonyms: Optional[list[str]] = Field(default=None, description="""Alternative names or synonyms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Drug',
                       'MolecularFunction'],
         'slot_uri': 'skos:altLabel'} })
    xrefs: Optional[list[str]] = Field(default=None, description="""Cross-references to external resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'MolecularFunction',
                       'Phenotype'],
         'slot_uri': 'biolink:xref'} })
    ontology: Optional[str] = Field(default=None, description="""Metadata about the source ontology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'MolecularFunction',
                       'Phenotype']} })


class PathogenicMechanism(AnalyticalEntity):
    """
    A biological mechanism that contributes to ALS initiation, progression, cellular dysfunction, or phenotype, such as TDP-43 proteinopathy, SOD1 toxic gain of function, C9orf72 repeat expansion toxicity, impaired RNA metabolism, mitochondrial dysfunction, oxidative stress, neuroinflammation, excitotoxicity, or impaired proteostasis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'PGM'}},
         'class_uri': 'alskg:PathogenicMechanism',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    has_pathogenic_mechanism_category: Optional[PathogenicMechanismEnum] = Field(default=None, description="""Categorizes a pathogenic mechanism using a controlled ALS mechanism category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenicMechanism'],
         'slot_uri': 'alskg:has_pathogenic_mechanism_category'} })
    involves_biological_process: Optional[list[str]] = Field(default=None, description="""Connects a pathogenic mechanism to a biological process it involves.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenicMechanism'], 'slot_uri': 'RO:0000056'} })
    involves_molecular_function: Optional[list[str]] = Field(default=None, description="""Connects a pathogenic mechanism to a molecular function it involves.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenicMechanism'],
         'slot_uri': 'alskg:involves_molecular_function'} })
    affects_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or result to an affected anatomical structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'RO:0002131'} })
    involves_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a disease, subtype, mechanism, or observation to a relevant cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'ALSSubtype',
                       'PathogenicMechanism'],
         'slot_uri': 'alskg:involves_cell_type'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    pathogenic_mechanism_occurs_in_cell_type: Optional[str] = Field(default=None, description="""Connects a pathogenic mechanism to the cell type where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenicMechanism'],
         'slot_uri': 'alskg:pathogenic_mechanism_occurs_in_cell_type'} })
    pathogenic_mechanism_occurs_in_anatomy: Optional[str] = Field(default=None, description="""Connects a pathogenic mechanism to the anatomy where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenicMechanism'],
         'slot_uri': 'alskg:pathogenic_mechanism_occurs_in_anatomy'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class MolecularEvent(AnalyticalEntity):
    """
    A specific molecular event involved in ALS pathogenesis, such as TDP-43 nuclear depletion, cytoplasmic aggregation, altered splicing, repeat RNA foci formation, DPR protein accumulation, mitochondrial complex dysregulation, or complement activation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'MEV'}},
         'class_uri': 'alskg:MolecularEvent',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    contributes_to_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects a gene, variant, protein, molecular event, or statement to a pathogenic mechanism it contributes to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein', 'MolecularEvent', 'PathogenesisStatement'],
         'slot_uri': 'alskg:contributes_to_pathogenic_mechanism'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class ProteinAggregate(PhysicalEntity):
    """
    An abnormal protein aggregate or pathological inclusion relevant to ALS, such as phosphorylated TDP-43 inclusions, SOD1 aggregates, FUS inclusions, or dipeptide-repeat protein aggregates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'PAG'}},
         'class_uri': 'alskg:ProteinAggregate',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    has_protein_component: Optional[list[str]] = Field(default=None, description="""Connects a protein aggregate to the protein components present in the aggregate.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinAggregate'], 'slot_uri': 'RO:0002180'} })
    occurs_in_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the cell type where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_cell_type'} })
    occurs_in_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the anatomy where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_anatomy'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class EvidenceStatement(AnalyticalEntity):
    """
    A reified, evidence-backed assertion in ALS-KG. Use statement/result nodes when the claim depends on subtype, tissue, cell type, cohort, assay, statistical support, or publication evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'EST'}},
         'class_uri': 'rdf:Statement',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    derives_from_dataset: Optional[str] = Field(default=None, description="""Connects a result or statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    occurs_in_cohort: Optional[str] = Field(default=None, description="""Connects a statement, result, or observation to a cohort in which it was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'PhenotypeObservation'],
         'slot_uri': 'alskg:occurs_in_cohort'} })
    confidence_score: Optional[float] = Field(default=None, description="""Numeric confidence score for an assertion or result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'EvidenceStatement'],
         'slot_uri': 'alskg:confidence_score'} })
    evidence_statement_supported_by_evidence: Optional[str] = Field(default=None, description="""Connects an evidence statement to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_supported_by_evidence'} })
    evidence_statement_derives_from_dataset: Optional[str] = Field(default=None, description="""Connects an evidence statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_derives_from_dataset'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class PathogenesisStatement(EvidenceStatement):
    """
    An evidence-backed assertion connecting a gene, variant, protein, molecular event, subtype, anatomy, or cell type to an ALS pathogenic mechanism.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'PSTMT'}},
         'class_uri': 'alskg:PathogenesisStatement',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    contributes_to_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects a gene, variant, protein, molecular event, or statement to a pathogenic mechanism it contributes to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Gene', 'Protein', 'MolecularEvent', 'PathogenesisStatement'],
         'slot_uri': 'alskg:contributes_to_pathogenic_mechanism'} })
    occurs_in_disease_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its disease context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_disease_context'} })
    occurs_in_subtype_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its ALS subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_subtype_context'} })
    occurs_in_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the cell type where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_cell_type'} })
    occurs_in_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the anatomy where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_anatomy'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    derives_from_dataset: Optional[str] = Field(default=None, description="""Connects a result or statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    occurs_in_cohort: Optional[str] = Field(default=None, description="""Connects a statement, result, or observation to a cohort in which it was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'PhenotypeObservation'],
         'slot_uri': 'alskg:occurs_in_cohort'} })
    confidence_score: Optional[float] = Field(default=None, description="""Numeric confidence score for an assertion or result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'EvidenceStatement'],
         'slot_uri': 'alskg:confidence_score'} })
    evidence_statement_supported_by_evidence: Optional[str] = Field(default=None, description="""Connects an evidence statement to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_supported_by_evidence'} })
    evidence_statement_derives_from_dataset: Optional[str] = Field(default=None, description="""Connects an evidence statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_derives_from_dataset'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class DifferentialExpressionStatement(EvidenceStatement):
    """
    A differential gene-expression assertion in an ALS context, including direction, comparator, subtype, anatomy, cell type, cohort, sample, assay, dataset, and statistical support. This is the semantic parent for the Neo4j-compatible GeneExpressionContext class.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'DER'}},
         'class_uri': 'alskg:DifferentialExpressionStatement',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    measures_gene_expression_of: Optional[str] = Field(default=None, description="""Connects a differential expression result to the gene whose expression is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext', 'DifferentialExpressionStatement'],
         'slot_uri': 'alskg:measures_gene_expression_of'} })
    has_expression_direction: Optional[ExpressionDirectionEnum] = Field(default=None, description="""Direction of differential expression relative to a comparator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext', 'DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_expression_direction'} })
    has_log_fold_change: Optional[float] = Field(default=None, description="""Log fold-change value for a differential expression result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_log_fold_change'} })
    has_p_value: Optional[float] = Field(default=None, description="""Nominal p-value for a statistical result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_p_value'} })
    has_adjusted_p_value: Optional[float] = Field(default=None, description="""Multiple-testing-adjusted p-value for a statistical result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_adjusted_p_value'} })
    has_false_discovery_rate: Optional[float] = Field(default=None, description="""False discovery rate for a statistical result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_false_discovery_rate'} })
    compares_against: Optional[str] = Field(default=None, description="""Connects a result to the comparator group or condition used in the analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:compares_against'} })
    occurs_in_disease_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its disease context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_disease_context'} })
    occurs_in_subtype_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its ALS subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_subtype_context'} })
    occurs_in_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the cell type where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_cell_type'} })
    occurs_in_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the anatomy where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_anatomy'} })
    occurs_in_cohort: Optional[str] = Field(default=None, description="""Connects a statement, result, or observation to a cohort in which it was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'PhenotypeObservation'],
         'slot_uri': 'alskg:occurs_in_cohort'} })
    measured_in_sample: Optional[str] = Field(default=None, description="""Connects a result to the biological sample measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:measured_in_sample'} })
    measured_by_assay: Optional[str] = Field(default=None, description="""Connects a result, biomarker, or observation to the assay that measured it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'Biomarker'],
         'slot_uri': 'OBI:0000293'} })
    derives_from_dataset: Optional[str] = Field(default=None, description="""Connects a result or statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    differential_expression_measures_gene: Optional[str] = Field(default=None, description="""Connects a differential expression statement to the gene measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_measures_gene'} })
    differential_expression_occurs_in_subtype: Optional[str] = Field(default=None, description="""Connects a differential expression result to its ALS subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_occurs_in_subtype'} })
    differential_expression_occurs_in_anatomy: Optional[str] = Field(default=None, description="""Connects a differential expression result to its anatomical context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_occurs_in_anatomy'} })
    differential_expression_occurs_in_cell_type: Optional[str] = Field(default=None, description="""Connects a differential expression result to its cell type context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_occurs_in_cell_type'} })
    differential_expression_measured_by_assay: Optional[str] = Field(default=None, description="""Connects a differential expression result to the assay that measured it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_measured_by_assay'} })
    differential_expression_derives_from_dataset: Optional[str] = Field(default=None, description="""Connects a differential expression result to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_derives_from_dataset'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    confidence_score: Optional[float] = Field(default=None, description="""Numeric confidence score for an assertion or result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'EvidenceStatement'],
         'slot_uri': 'alskg:confidence_score'} })
    evidence_statement_supported_by_evidence: Optional[str] = Field(default=None, description="""Connects an evidence statement to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_supported_by_evidence'} })
    evidence_statement_derives_from_dataset: Optional[str] = Field(default=None, description="""Connects an evidence statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_derives_from_dataset'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class GeneExpressionContext(DifferentialExpressionStatement):
    """
    Neo4j-compatible concrete expression-context node for ALS-KG. Prefer the parent class DifferentialExpressionStatement for ontology semantics; use GeneExpressionContext when materializing expression findings as Neo4j nodes such as ECX.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'ECX'},
                         'source_note': {'tag': 'source_note',
                                         'value': 'Primary data from '
                                                  'NIHMS2069122-supplement-5.xlsx '
                                                  'TableS3A (NYGC ALS Consortium '
                                                  'postmortem cortex and cord) and '
                                                  'TableS3E (Ziff et al. 2023 iPSC '
                                                  'motor neuron models). Replaces the '
                                                  'binary DYSREGULATED_IN edge '
                                                  '(GEN->MST).'}},
         'class_uri': 'alskg:GeneExpressionContext',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    source: Optional[str] = Field(default=None, description="""Source string or compact source identifier, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    measures_gene_expression_of: Optional[str] = Field(default=None, description="""Connects a differential expression result to the gene whose expression is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext', 'DifferentialExpressionStatement'],
         'slot_uri': 'alskg:measures_gene_expression_of'} })
    has_expression_direction: Optional[ExpressionDirectionEnum] = Field(default=None, description="""Direction of differential expression relative to a comparator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext', 'DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_expression_direction'} })
    occurs_in_subtype_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its ALS subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_subtype_context'} })
    occurs_in_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the cell type where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_cell_type'} })
    occurs_in_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the anatomy where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_anatomy'} })
    measured_in_sample: Optional[str] = Field(default=None, description="""Connects a result to the biological sample measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:measured_in_sample'} })
    measured_by_assay: Optional[str] = Field(default=None, description="""Connects a result, biomarker, or observation to the assay that measured it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'Biomarker'],
         'slot_uri': 'OBI:0000293'} })
    derives_from_dataset: Optional[str] = Field(default=None, description="""Connects a result or statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    gene: str = Field(default=..., description="""The gene or genomic feature whose expression is described by this context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext'], 'slot_uri': 'RO:0002206'} })
    molecular_subtype: str = Field(default=..., description="""The molecular disease subtype in which the gene is differentially expressed (e.g. ALS-Ox, ALS-Glia, ALS-TE).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext'], 'slot_uri': 'okg:in_molecular_subtype'} })
    anatomy: Optional[str] = Field(default=None, description="""The tissue or anatomical region in which the expression was measured (e.g. motor cortex, spinal cord). Null when the context is an iPSC cell model without a corresponding anatomy node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext'], 'slot_uri': 'okg:in_anatomy'} })
    direction: ExpressionDirectionEnum = Field(default=..., description="""Direction of differential expression relative to non-ALS controls. UP = upregulated; DOWN = downregulated in this molecular subtype and biological context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext']} })
    biological_context_type: Optional[BiologicalContextTypeEnum] = Field(default=None, description="""Type of biological context in which the expression was measured (e.g. postmortem_cortex, postmortem_cord, C9orf72_motor_neuron).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext']} })
    cell_model: Optional[str] = Field(default=None, description="""Specific iPSC cell model identifier when the context is a cell model rather than postmortem tissue (e.g. \"C9orf72_motor_neuron\", \"FUS_motor_neuron\", \"TDP43_motor_neuron\"). Null for postmortem tissue.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext']} })
    year: Optional[int] = Field(default=None, description="""Year of the study providing this expression evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext']} })
    validated_in: Optional[list[str]] = Field(default=None, description="""Independent studies in which this expression finding has been replicated or cross-validated (e.g. \"Catanese_2023\", \"Ho_2021\", \"Humphrey_2022\", \"Ziff_2023\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext']} })
    biological_note: Optional[str] = Field(default=None, description="""Optional free-text note contextualizing the biological significance of this expression finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext']} })
    has_log_fold_change: Optional[float] = Field(default=None, description="""Log fold-change value for a differential expression result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_log_fold_change'} })
    has_p_value: Optional[float] = Field(default=None, description="""Nominal p-value for a statistical result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_p_value'} })
    has_adjusted_p_value: Optional[float] = Field(default=None, description="""Multiple-testing-adjusted p-value for a statistical result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_adjusted_p_value'} })
    has_false_discovery_rate: Optional[float] = Field(default=None, description="""False discovery rate for a statistical result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:has_false_discovery_rate'} })
    compares_against: Optional[str] = Field(default=None, description="""Connects a result to the comparator group or condition used in the analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:compares_against'} })
    occurs_in_disease_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its disease context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_disease_context'} })
    occurs_in_cohort: Optional[str] = Field(default=None, description="""Connects a statement, result, or observation to a cohort in which it was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'PhenotypeObservation'],
         'slot_uri': 'alskg:occurs_in_cohort'} })
    differential_expression_measures_gene: Optional[str] = Field(default=None, description="""Connects a differential expression statement to the gene measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_measures_gene'} })
    differential_expression_occurs_in_subtype: Optional[str] = Field(default=None, description="""Connects a differential expression result to its ALS subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_occurs_in_subtype'} })
    differential_expression_occurs_in_anatomy: Optional[str] = Field(default=None, description="""Connects a differential expression result to its anatomical context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_occurs_in_anatomy'} })
    differential_expression_occurs_in_cell_type: Optional[str] = Field(default=None, description="""Connects a differential expression result to its cell type context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_occurs_in_cell_type'} })
    differential_expression_measured_by_assay: Optional[str] = Field(default=None, description="""Connects a differential expression result to the assay that measured it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_measured_by_assay'} })
    differential_expression_derives_from_dataset: Optional[str] = Field(default=None, description="""Connects a differential expression result to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DifferentialExpressionStatement'],
         'slot_uri': 'alskg:differential_expression_derives_from_dataset'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    confidence_score: Optional[float] = Field(default=None, description="""Numeric confidence score for an assertion or result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'EvidenceStatement'],
         'slot_uri': 'alskg:confidence_score'} })
    evidence_statement_supported_by_evidence: Optional[str] = Field(default=None, description="""Connects an evidence statement to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_supported_by_evidence'} })
    evidence_statement_derives_from_dataset: Optional[str] = Field(default=None, description="""Connects an evidence statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_derives_from_dataset'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })


class ProteinAbundanceResult(EvidenceStatement):
    """
    A protein abundance, localization, or pathology result in an ALS context, including protein, aggregate, tissue, cell type, assay, cohort, and evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'PAR'}},
         'class_uri': 'alskg:ProteinAbundanceResult',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    measures_protein_abundance_of: Optional[str] = Field(default=None, description="""Connects a protein abundance result to the protein measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinAbundanceResult'],
         'slot_uri': 'alskg:measures_protein_abundance_of'} })
    has_abundance_direction: Optional[ExpressionDirectionEnum] = Field(default=None, description="""Direction of protein abundance change relative to comparator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProteinAbundanceResult'],
         'slot_uri': 'alskg:has_abundance_direction'} })
    occurs_in_disease_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its disease context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_disease_context'} })
    occurs_in_subtype_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its ALS subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_subtype_context'} })
    occurs_in_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the cell type where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_cell_type'} })
    occurs_in_anatomy: Optional[list[str]] = Field(default=None, description="""Connects a mechanism, event, statement, or result to the anatomy where it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'ProteinAggregate',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:occurs_in_anatomy'} })
    measured_in_sample: Optional[str] = Field(default=None, description="""Connects a result to the biological sample measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'alskg:measured_in_sample'} })
    measured_by_assay: Optional[str] = Field(default=None, description="""Connects a result, biomarker, or observation to the assay that measured it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'Biomarker'],
         'slot_uri': 'OBI:0000293'} })
    derives_from_dataset: Optional[str] = Field(default=None, description="""Connects a result or statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    occurs_in_cohort: Optional[str] = Field(default=None, description="""Connects a statement, result, or observation to a cohort in which it was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'PhenotypeObservation'],
         'slot_uri': 'alskg:occurs_in_cohort'} })
    confidence_score: Optional[float] = Field(default=None, description="""Numeric confidence score for an assertion or result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'EvidenceStatement'],
         'slot_uri': 'alskg:confidence_score'} })
    evidence_statement_supported_by_evidence: Optional[str] = Field(default=None, description="""Connects an evidence statement to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_supported_by_evidence'} })
    evidence_statement_derives_from_dataset: Optional[str] = Field(default=None, description="""Connects an evidence statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_derives_from_dataset'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class PhenotypeObservation(EvidenceStatement):
    """
    A contextual observation that a phenotype, symptom, sign, or clinical feature is present, absent, frequent, rare, early, late, or otherwise characterized in ALS or an ALS subtype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'POB'}},
         'class_uri': 'alskg:PhenotypeObservation',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    has_observed_phenotype: Optional[str] = Field(default=None, description="""Connects a phenotype observation to the phenotype observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservation'],
         'slot_uri': 'alskg:has_observed_phenotype'} })
    occurs_in_disease_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its disease context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_disease_context'} })
    occurs_in_subtype_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its ALS subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_subtype_context'} })
    has_disease_stage: Optional[str] = Field(default=None, description="""Connects an observation to a disease stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservation'], 'slot_uri': 'alskg:has_disease_stage'} })
    has_progression_pattern: Optional[str] = Field(default=None, description="""Connects an observation, subtype, or disease to a progression pattern.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservation'],
         'slot_uri': 'alskg:has_progression_pattern'} })
    occurs_in_cohort: Optional[str] = Field(default=None, description="""Connects a statement, result, or observation to a cohort in which it was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'PhenotypeObservation'],
         'slot_uri': 'alskg:occurs_in_cohort'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    phenotype_observation_has_observed_phenotype: Optional[str] = Field(default=None, description="""Connects a phenotype observation to the phenotype observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservation'],
         'slot_uri': 'alskg:phenotype_observation_has_observed_phenotype'} })
    phenotype_observation_occurs_in_subtype: Optional[str] = Field(default=None, description="""Connects a phenotype observation to its subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypeObservation'],
         'slot_uri': 'alskg:phenotype_observation_occurs_in_subtype'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    derives_from_dataset: Optional[str] = Field(default=None, description="""Connects a result or statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    confidence_score: Optional[float] = Field(default=None, description="""Numeric confidence score for an assertion or result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'EvidenceStatement'],
         'slot_uri': 'alskg:confidence_score'} })
    evidence_statement_supported_by_evidence: Optional[str] = Field(default=None, description="""Connects an evidence statement to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_supported_by_evidence'} })
    evidence_statement_derives_from_dataset: Optional[str] = Field(default=None, description="""Connects an evidence statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_derives_from_dataset'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class DiseaseStage(ClinicalEntity):
    """
    A temporal or clinical stage of ALS, such as early disease, established disease, late disease, pre-symptomatic carrier state, or time since symptom onset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'DST'}},
         'class_uri': 'alskg:DiseaseStage',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class ProgressionPattern(ClinicalEntity):
    """
    A disease progression pattern such as fast progression, slow progression, respiratory progression, spreading pattern, or ALSFRS-R decline trajectory.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'PRG'}},
         'class_uri': 'alskg:ProgressionPattern',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class Biomarker(ClinicalEntity):
    """
    A molecular, imaging, electrophysiological, pathological, or clinical biomarker relevant to ALS diagnosis, subtype, prognosis, progression, mechanism, or therapeutic response.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'BMK'}},
         'class_uri': 'biolink:Biomarker',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    biomarker_for_disease: Optional[list[str]] = Field(default=None, description="""Connects a biomarker to a disease it marks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Biomarker'], 'slot_uri': 'biolink:biomarker_for'} })
    biomarker_for_subtype: Optional[list[str]] = Field(default=None, description="""Connects a biomarker to an ALS subtype it marks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Biomarker'], 'slot_uri': 'alskg:biomarker_for_subtype'} })
    indicates_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects a biomarker to a pathogenic mechanism it indicates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Biomarker'], 'slot_uri': 'alskg:indicates_pathogenic_mechanism'} })
    measured_by_assay: Optional[str] = Field(default=None, description="""Connects a result, biomarker, or observation to the assay that measured it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'Biomarker'],
         'slot_uri': 'OBI:0000293'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class Study(ProvenanceEntity):
    """
    A research study generating ALS evidence, datasets, cohorts, measurements, or publications.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'STU'}},
         'class_uri': 'OBI:0000066',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    has_publication: Optional[list[str]] = Field(default=None, description="""Connects an evidence record or statement to a supporting publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'Study', 'Dataset', 'ClinicalTrial'],
         'slot_uri': 'biolink:publications'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class Dataset(ProvenanceEntity):
    """
    A dataset used as evidence or source for ALS-KG statements, such as Target ALS, Answer ALS, NYGC ALS, Project MinE, ALL ALS, or GEO studies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'DAT'}},
         'class_uri': 'schema:Dataset',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    has_publication: Optional[list[str]] = Field(default=None, description="""Connects an evidence record or statement to a supporting publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'Study', 'Dataset', 'ClinicalTrial'],
         'slot_uri': 'biolink:publications'} })


class Cohort(ProvenanceEntity):
    """
    A participant group, case/control group, genotype group, subtype group, or study cohort used in ALS research.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'COH'}},
         'class_uri': 'OBI:0000202',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class ComparatorGroup(Cohort):
    """
    A comparator group used in differential expression, biomarker, or clinical analyses, such as control, non-ALS, sporadic ALS, C9orf72-ALS, or healthy motor neuron group.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'CMP'}},
         'class_uri': 'alskg:ComparatorGroup',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class Sample(ProvenanceEntity):
    """
    A biological sample or specimen used in ALS analysis, such as postmortem spinal cord, motor cortex, CSF, blood, iPSC-derived motor neurons, or sorted cell populations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'SMP'}},
         'class_uri': 'OBI:0100051',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    derived_from_anatomy: Optional[str] = Field(default=None, description="""Connects a sample to the anatomy from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'RO:0001000'} })
    has_cell_type: Optional[list[str]] = Field(default=None, description="""Connects a sample or context to its cell type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'alskg:has_cell_type'} })
    occurs_in_disease_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its disease context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_disease_context'} })
    occurs_in_subtype_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its ALS subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_subtype_context'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class Assay(ProvenanceEntity):
    """
    An assay or measurement method used to generate ALS evidence, such as bulk RNA-seq, single-nucleus RNA-seq, spatial transcriptomics, proteomics, WGS, immunostaining, or clinical assessment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'ASY'}},
         'class_uri': 'OBI:0000070',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })


class ModelSystem(AnalyticalEntity):
    """
    A biological model system used to study ALS, including animal models, iPSC-derived cells, organoids, cell lines, or perturbation systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'MOD'}},
         'class_uri': 'alskg:ModelSystem',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    models_disease: Optional[str] = Field(default=None, description="""Connects a model system to the disease it models.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelSystem'], 'slot_uri': 'alskg:models_disease'} })
    models_subtype: Optional[str] = Field(default=None, description="""Connects a model system to the ALS subtype it models.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelSystem'], 'slot_uri': 'alskg:models_subtype'} })
    has_genetic_perturbation: Optional[list[str]] = Field(default=None, description="""Connects a model system to a gene, variant, or perturbation used in the model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelSystem'], 'slot_uri': 'alskg:has_genetic_perturbation'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    model_system_models_subtype: Optional[str] = Field(default=None, description="""Connects a model system to the ALS subtype it models.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ModelSystem'], 'slot_uri': 'alskg:model_system_models_subtype'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class TherapeuticIntervention(ClinicalEntity):
    """
    A therapeutic intervention relevant to ALS, including small molecules, antisense oligonucleotides, gene therapy, biologics, rehabilitation, respiratory support, or investigational therapies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'TX'}},
         'class_uri': 'biolink:Treatment',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    targets_gene: Optional[list[str]] = Field(default=None, description="""Connects a drug, intervention, or hypothesis to a target gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'TherapeuticIntervention', 'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:targets_gene'} })
    targets_protein: Optional[list[str]] = Field(default=None, description="""Connects a drug, intervention, or hypothesis to a target protein.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'TherapeuticIntervention', 'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:targets_protein'} })
    modulates_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects a drug/intervention/hypothesis to the pathogenic mechanism it modulates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'TherapeuticIntervention', 'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:modulates_pathogenic_mechanism'} })
    tested_in_clinical_trial: Optional[list[str]] = Field(default=None, description="""Connects a therapy or intervention to a clinical trial that tests it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TherapeuticIntervention'],
         'slot_uri': 'alskg:tested_in_clinical_trial'} })
    therapeutic_intervention_tested_in_clinical_trial: Optional[str] = Field(default=None, description="""Connects a therapeutic intervention to a clinical trial that tests it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TherapeuticIntervention'],
         'slot_uri': 'alskg:therapeutic_intervention_tested_in_clinical_trial'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })


class ClinicalTrial(Study):
    """
    A clinical trial or interventional study relevant to ALS, ALS subtypes, therapies, biomarkers, or outcomes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'TRI'}},
         'class_uri': 'biolink:ClinicalTrial',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    tests_intervention: Optional[list[str]] = Field(default=None, description="""Connects a clinical trial to the intervention it tests.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial'], 'slot_uri': 'alskg:tests_intervention'} })
    enrolls_subtype: Optional[list[str]] = Field(default=None, description="""Connects a clinical trial to an enrolled or targeted ALS subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial'], 'slot_uri': 'alskg:enrolls_subtype'} })
    has_outcome_measure: Optional[list[str]] = Field(default=None, description="""Connects a clinical trial to an outcome measure or endpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial'], 'slot_uri': 'alskg:has_outcome_measure'} })
    has_publication: Optional[list[str]] = Field(default=None, description="""Connects an evidence record or statement to a supporting publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'Study', 'Dataset', 'ClinicalTrial'],
         'slot_uri': 'biolink:publications'} })
    clinical_trial_enrolls_subtype: Optional[str] = Field(default=None, description="""Connects a clinical trial to an ALS subtype that it enrolls or targets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClinicalTrial'],
         'slot_uri': 'alskg:clinical_trial_enrolls_subtype'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class DrugRepurposingHypothesis(EvidenceStatement):
    """
    A hypothesis that a drug or therapeutic intervention may be relevant to ALS or an ALS subtype based on target genes, disease mechanisms, expression directionality, pathways, biomarkers, model evidence, or clinical evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'DRH'}},
         'class_uri': 'alskg:DrugRepurposingHypothesis',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    prioritizes_drug: Optional[str] = Field(default=None, description="""Connects a drug repurposing hypothesis to the candidate drug being prioritized.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:prioritizes_drug'} })
    targets_gene: Optional[list[str]] = Field(default=None, description="""Connects a drug, intervention, or hypothesis to a target gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'TherapeuticIntervention', 'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:targets_gene'} })
    targets_protein: Optional[list[str]] = Field(default=None, description="""Connects a drug, intervention, or hypothesis to a target protein.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'TherapeuticIntervention', 'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:targets_protein'} })
    modulates_pathogenic_mechanism: Optional[list[str]] = Field(default=None, description="""Connects a drug/intervention/hypothesis to the pathogenic mechanism it modulates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Drug', 'TherapeuticIntervention', 'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:modulates_pathogenic_mechanism'} })
    occurs_in_disease_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its disease context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_disease_context'} })
    occurs_in_subtype_context: Optional[str] = Field(default=None, description="""Connects a statement or result to its ALS subtype context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Sample',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:occurs_in_subtype_context'} })
    has_evidence_basis: Optional[list[str]] = Field(default=None, description="""Connects a hypothesis to evidence statements used as its rationale.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:has_evidence_basis'} })
    is_supported_by: Optional[list[str]] = Field(default=None, description="""Connects a statement, observation, subtype, or hypothesis to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Phenotype',
                       'MolecularSubtype',
                       'GeneExpressionContext',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'Biomarker',
                       'ModelSystem',
                       'DrugRepurposingHypothesis'],
         'slot_uri': 'RO:0002558'} })
    drug_repurposing_hypothesis_prioritizes_drug: Optional[str] = Field(default=None, description="""Connects a drug repurposing hypothesis to the candidate drug being prioritized.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:drug_repurposing_hypothesis_prioritizes_drug'} })
    drug_repurposing_hypothesis_targets_gene: Optional[str] = Field(default=None, description="""Connects a drug repurposing hypothesis to an implicated target gene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:drug_repurposing_hypothesis_targets_gene'} })
    drug_repurposing_hypothesis_modulates_pathogenic_mechanism: Optional[str] = Field(default=None, description="""Connects a drug repurposing hypothesis to a pathogenic mechanism it proposes to modulate.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DrugRepurposingHypothesis'],
         'slot_uri': 'alskg:drug_repurposing_hypothesis_modulates_pathogenic_mechanism'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    derives_from_dataset: Optional[str] = Field(default=None, description="""Connects a result or statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpressionContext',
                       'EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    occurs_in_cohort: Optional[str] = Field(default=None, description="""Connects a statement, result, or observation to a cohort in which it was observed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement',
                       'DifferentialExpressionStatement',
                       'PhenotypeObservation'],
         'slot_uri': 'alskg:occurs_in_cohort'} })
    confidence_score: Optional[float] = Field(default=None, description="""Numeric confidence score for an assertion or result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceRecord', 'EvidenceStatement'],
         'slot_uri': 'alskg:confidence_score'} })
    evidence_statement_supported_by_evidence: Optional[str] = Field(default=None, description="""Connects an evidence statement to supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_supported_by_evidence'} })
    evidence_statement_derives_from_dataset: Optional[str] = Field(default=None, description="""Connects an evidence statement to the dataset from which it was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceStatement'],
         'slot_uri': 'alskg:evidence_statement_derives_from_dataset'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class BiologicalAgent(Exposure):
    """
    Optional ALS-KG class for infectious, microbiome, or biological exposure agents if these are intentionally modeled. For ALS pathogenesis, prefer PathogenicMechanism rather than BiologicalAgent unless the assertion is truly about an organism or biological exposure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'recommended_neo4j_label': {'tag': 'recommended_neo4j_label',
                                                     'value': 'BAG'}},
         'class_uri': 'alskg:BiologicalAgent',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Exposure name (MeSH preferred term, e.g. \"Benzo(a)pyrene\", \"Arsenic\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    has_synonym: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured Synonym node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'skos:altLabel'} })
    has_cross_reference: Optional[list[str]] = Field(default=None, description="""Connects an entity to a structured CrossReference or DatabaseAccession node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'MolecularSubtype',
                       'AmyotrophicLateralSclerosis',
                       'CellType'],
         'slot_uri': 'biolink:xref'} })
    source_categories: Optional[list[str]] = Field(default=None, description="""Categories describing the origin or context of the exposure (e.g. \"chemical\", \"biological\", \"physical\", \"dietary\", \"lifestyle\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })
    source_details: Optional[str] = Field(default=None, description="""Free-text description providing additional source-specific context for the exposure (e.g. specific exposure routes, measurement context)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Exposure']} })


class ALSRelationship(RelationshipAssertion):
    """
    Abstract parent for ALS-KG extension relationships that can be materialized in Neo4j while preserving OptimusKG compatibility.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'alskg:ALSRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeRelationship(ALSRelationship):
    """
    Relationships defining, classifying, or contextualizing ALS subtypes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'alskg:ALSSubtypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSPathogenesisRelationship(ALSRelationship):
    """
    Relationships connecting genes, variants, proteins, subtypes, mechanisms, cell types, and anatomy in ALS pathogenesis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'alskg:ALSPathogenesisRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSExpressionRelationship(ALSRelationship):
    """
    Relationships connecting differential expression results to genes, subtype, anatomy, cell type, sample, assay, cohort, dataset, and evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'alskg:ALSExpressionRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSEvidenceRelationship(ALSRelationship):
    """
    Relationships connecting ALS-KG statements, results, subtypes, and hypotheses to studies, datasets, cohorts, samples, assays, publications, and evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'alskg:ALSEvidenceRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSTherapeuticRelationship(ALSRelationship):
    """
    Relationships supporting ALS therapeutic intervention, target, clinical trial, and drug repurposing hypotheses.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'alskg:ALSTherapeuticRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DiseaseHasALSSubtypeRelationship(ALSSubtypeRelationship):
    """
    Disease-to-subtype relationship meaning the disease has the ALS subtype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'disease_has_als_subtype'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_ALS_SUBTYPE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DiseaseHasALSSubtypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'ALSSubtype'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_ALS_SUBTYPE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'Disease'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeIsSubtypeOfDiseaseRelationship(ALSSubtypeRelationship):
    """
    Subtype-to-disease relationship meaning the ALS subtype is a subtype of the disease.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'als_subtype_is_subtype_of_disease'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'IS_SUBTYPE_OF'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ALSSubtypeIsSubtypeOfDiseaseRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Disease'},
                        'original_optimus_relationship_type': {'equals_string': 'IS_SUBTYPE_OF',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ALSSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeHasSubtypeSchemeRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to its subtype scheme or taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'als_subtype_has_subtype_scheme'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_SUBTYPE_SCHEME'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ALSSubtypeHasSubtypeSchemeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'SubtypeScheme'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_SUBTYPE_SCHEME',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ALSSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeHasSubtypeCriterionRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to a defining or assignment criterion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'als_subtype_has_subtype_criterion'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_SUBTYPE_CRITERION'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ALSSubtypeHasSubtypeCriterionRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'SubtypeCriterion'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_SUBTYPE_CRITERION',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ALSSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeDefinedByGeneRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to a defining or characteristic gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'als_subtype_defined_by_gene'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'DEFINED_BY_GENE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ALSSubtypeDefinedByGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'DEFINED_BY_GENE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ALSSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeDefinedByVariantRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to a defining or characteristic variant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'als_subtype_defined_by_variant'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'DEFINED_BY_VARIANT'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ALSSubtypeDefinedByVariantRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'SequenceVariant'},
                        'original_optimus_relationship_type': {'equals_string': 'DEFINED_BY_VARIANT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ALSSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeHasPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects an ALS subtype to a pathogenic mechanism implicated in that subtype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'als_subtype_has_pathogenic_mechanism'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_PATHOGENIC_MECHANISM'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ALSSubtypeHasPathogenicMechanismRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'PathogenicMechanism'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_PATHOGENIC_MECHANISM',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ALSSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeAffectsAnatomyRelationship(ALSPathogenesisRelationship):
    """
    Connects an ALS subtype to an affected anatomical structure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'als_subtype_affects_anatomy'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'AFFECTS_ANATOMY'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ALSSubtypeAffectsAnatomyRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Anatomy'},
                        'original_optimus_relationship_type': {'equals_string': 'AFFECTS_ANATOMY',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ALSSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeInvolvesCellTypeRelationship(ALSPathogenesisRelationship):
    """
    Connects an ALS subtype to a relevant or affected cell type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'als_subtype_involves_cell_type'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INVOLVES_CELL_TYPE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ALSSubtypeInvolvesCellTypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'CellType'},
                        'original_optimus_relationship_type': {'equals_string': 'INVOLVES_CELL_TYPE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ALSSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSSubtypeHasPhenotypeObservationRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to a contextual phenotype observation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'als_subtype_has_phenotype_observation'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_PHENOTYPE_OBSERVATION'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ALSSubtypeHasPhenotypeObservationRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'PhenotypeObservation'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_PHENOTYPE_OBSERVATION',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ALSSubtype'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class GeneHasVariantRelationship(ALSPathogenesisRelationship):
    """
    Connects a gene to a sequence variant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'gene_has_variant'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_VARIANT'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:GeneHasVariantRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'SequenceVariant'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_VARIANT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'Gene'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class VariantAffectsGeneRelationship(ALSPathogenesisRelationship):
    """
    Connects a sequence variant to the gene it affects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'variant_affects_gene'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'AFFECTS_GENE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:VariantAffectsGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'AFFECTS_GENE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'SequenceVariant'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class VariantAltersProteinRelationship(ALSPathogenesisRelationship):
    """
    Connects a sequence variant to a protein it alters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'variant_alters_protein'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ALTERS_PROTEIN'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:VariantAltersProteinRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Protein'},
                        'original_optimus_relationship_type': {'equals_string': 'ALTERS_PROTEIN',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'SequenceVariant'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class GeneContributesToPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects a gene to an ALS pathogenic mechanism it contributes to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'gene_contributes_to_pathogenic_mechanism'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'CONTRIBUTES_TO_PATHOGENIC_MECHANISM'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:GeneContributesToPathogenicMechanismRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'PathogenicMechanism'},
                        'original_optimus_relationship_type': {'equals_string': 'CONTRIBUTES_TO_PATHOGENIC_MECHANISM',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'Gene'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ProteinContributesToPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects a protein to an ALS pathogenic mechanism it contributes to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'protein_contributes_to_pathogenic_mechanism'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'CONTRIBUTES_TO_PATHOGENIC_MECHANISM'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ProteinContributesToPathogenicMechanismRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'PathogenicMechanism'},
                        'original_optimus_relationship_type': {'equals_string': 'CONTRIBUTES_TO_PATHOGENIC_MECHANISM',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'Protein'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class MolecularEventContributesToPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects a molecular event to the pathogenic mechanism it contributes to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'molecular_event_contributes_to_pathogenic_mechanism'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'CONTRIBUTES_TO_PATHOGENIC_MECHANISM'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:MolecularEventContributesToPathogenicMechanismRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'PathogenicMechanism'},
                        'original_optimus_relationship_type': {'equals_string': 'CONTRIBUTES_TO_PATHOGENIC_MECHANISM',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'MolecularEvent'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PathogenicMechanismOccursInCellTypeRelationship(ALSPathogenesisRelationship):
    """
    Connects a pathogenic mechanism to the cell type where it occurs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'pathogenic_mechanism_occurs_in_cell_type'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'OCCURS_IN_CELL_TYPE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:PathogenicMechanismOccursInCellTypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'CellType'},
                        'original_optimus_relationship_type': {'equals_string': 'OCCURS_IN_CELL_TYPE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'PathogenicMechanism'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PathogenicMechanismOccursInAnatomyRelationship(ALSPathogenesisRelationship):
    """
    Connects a pathogenic mechanism to the anatomy where it occurs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'pathogenic_mechanism_occurs_in_anatomy'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'OCCURS_IN_ANATOMY'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:PathogenicMechanismOccursInAnatomyRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Anatomy'},
                        'original_optimus_relationship_type': {'equals_string': 'OCCURS_IN_ANATOMY',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'PathogenicMechanism'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DifferentialExpressionMeasuresGeneRelationship(ALSExpressionRelationship):
    """
    Connects a differential expression statement to the gene measured.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'differential_expression_measures_gene'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'MEASURES_GENE_EXPRESSION_OF'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DifferentialExpressionMeasuresGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'MEASURES_GENE_EXPRESSION_OF',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'DifferentialExpressionStatement'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DifferentialExpressionOccursInSubtypeRelationship(ALSExpressionRelationship):
    """
    Connects a differential expression result to its ALS subtype context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'differential_expression_occurs_in_subtype'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'OCCURS_IN_SUBTYPE_CONTEXT'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DifferentialExpressionOccursInSubtypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'ALSSubtype'},
                        'original_optimus_relationship_type': {'equals_string': 'OCCURS_IN_SUBTYPE_CONTEXT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'DifferentialExpressionStatement'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DifferentialExpressionOccursInAnatomyRelationship(ALSExpressionRelationship):
    """
    Connects a differential expression result to its anatomical context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'differential_expression_occurs_in_anatomy'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'OCCURS_IN_ANATOMY'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DifferentialExpressionOccursInAnatomyRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Anatomy'},
                        'original_optimus_relationship_type': {'equals_string': 'OCCURS_IN_ANATOMY',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'DifferentialExpressionStatement'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DifferentialExpressionOccursInCellTypeRelationship(ALSExpressionRelationship):
    """
    Connects a differential expression result to its cell type context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'differential_expression_occurs_in_cell_type'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'OCCURS_IN_CELL_TYPE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DifferentialExpressionOccursInCellTypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'CellType'},
                        'original_optimus_relationship_type': {'equals_string': 'OCCURS_IN_CELL_TYPE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'DifferentialExpressionStatement'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DifferentialExpressionMeasuredByAssayRelationship(ALSEvidenceRelationship):
    """
    Connects a differential expression result to the assay that measured it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'differential_expression_measured_by_assay'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'MEASURED_BY_ASSAY'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DifferentialExpressionMeasuredByAssayRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Assay'},
                        'original_optimus_relationship_type': {'equals_string': 'MEASURED_BY_ASSAY',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'DifferentialExpressionStatement'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DifferentialExpressionDerivedFromDatasetRelationship(ALSEvidenceRelationship):
    """
    Connects a differential expression result to the dataset from which it was derived.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'differential_expression_derives_from_dataset'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'DERIVES_FROM_DATASET'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DifferentialExpressionDerivedFromDatasetRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Dataset'},
                        'original_optimus_relationship_type': {'equals_string': 'DERIVES_FROM_DATASET',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'DifferentialExpressionStatement'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class EvidenceStatementSupportedByEvidenceRelationship(ALSEvidenceRelationship):
    """
    Connects an evidence statement to supporting evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'evidence_statement_supported_by_evidence'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'SUPPORTED_BY'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:EvidenceStatementSupportedByEvidenceRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'EvidenceRecord'},
                        'original_optimus_relationship_type': {'equals_string': 'SUPPORTED_BY',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'EvidenceStatement'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class EvidenceStatementDerivedFromDatasetRelationship(ALSEvidenceRelationship):
    """
    Connects an evidence statement to the dataset from which it was derived.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'evidence_statement_derives_from_dataset'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'DERIVES_FROM_DATASET'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:EvidenceStatementDerivedFromDatasetRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Dataset'},
                        'original_optimus_relationship_type': {'equals_string': 'DERIVES_FROM_DATASET',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'EvidenceStatement'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PhenotypeObservationHasObservedPhenotypeRelationship(ALSSubtypeRelationship):
    """
    Connects a phenotype observation to the phenotype observed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'phenotype_observation_has_observed_phenotype'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'HAS_OBSERVED_PHENOTYPE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:PhenotypeObservationHasObservedPhenotypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Phenotype'},
                        'original_optimus_relationship_type': {'equals_string': 'HAS_OBSERVED_PHENOTYPE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'PhenotypeObservation'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class PhenotypeObservationOccursInSubtypeRelationship(ALSSubtypeRelationship):
    """
    Connects a phenotype observation to its subtype context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'phenotype_observation_occurs_in_subtype'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'OCCURS_IN_SUBTYPE_CONTEXT'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:PhenotypeObservationOccursInSubtypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'ALSSubtype'},
                        'original_optimus_relationship_type': {'equals_string': 'OCCURS_IN_SUBTYPE_CONTEXT',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'PhenotypeObservation'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class BiomarkerIndicatesPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects a biomarker to a pathogenic mechanism it indicates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'biomarker_indicates_pathogenic_mechanism'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'INDICATES_PATHOGENIC_MECHANISM'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:BiomarkerIndicatesPathogenicMechanismRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'PathogenicMechanism'},
                        'original_optimus_relationship_type': {'equals_string': 'INDICATES_PATHOGENIC_MECHANISM',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'Biomarker'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugRepurposingHypothesisPrioritizesDrugRelationship(ALSTherapeuticRelationship):
    """
    Connects a drug repurposing hypothesis to the candidate drug being prioritized.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_repurposing_hypothesis_prioritizes_drug'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'PRIORITIZES_DRUG'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DrugRepurposingHypothesisPrioritizesDrugRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Drug'},
                        'original_optimus_relationship_type': {'equals_string': 'PRIORITIZES_DRUG',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'DrugRepurposingHypothesis'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugRepurposingHypothesisTargetsGeneRelationship(ALSTherapeuticRelationship):
    """
    Connects a drug repurposing hypothesis to an implicated target gene.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_repurposing_hypothesis_targets_gene'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'TARGETS_GENE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DrugRepurposingHypothesisTargetsGeneRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'Gene'},
                        'original_optimus_relationship_type': {'equals_string': 'TARGETS_GENE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'DrugRepurposingHypothesis'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship(ALSTherapeuticRelationship):
    """
    Connects a drug repurposing hypothesis to a pathogenic mechanism it proposes to modulate.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'drug_repurposing_hypothesis_modulates_pathogenic_mechanism'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'MODULATES_PATHOGENIC_MECHANISM'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'PathogenicMechanism'},
                        'original_optimus_relationship_type': {'equals_string': 'MODULATES_PATHOGENIC_MECHANISM',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'DrugRepurposingHypothesis'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class TherapeuticInterventionTestedInClinicalTrialRelationship(ALSTherapeuticRelationship):
    """
    Connects a therapeutic intervention to a clinical trial that tests it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'therapeutic_intervention_tested_in_clinical_trial'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'TESTED_IN_CLINICAL_TRIAL'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:TherapeuticInterventionTestedInClinicalTrialRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'ClinicalTrial'},
                        'original_optimus_relationship_type': {'equals_string': 'TESTED_IN_CLINICAL_TRIAL',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject',
                                    'range': 'TherapeuticIntervention'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ClinicalTrialEnrollsSubtypeRelationship(ALSTherapeuticRelationship):
    """
    Connects a clinical trial to an ALS subtype that it enrolls or targets.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'clinical_trial_enrolls_subtype'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'ENROLLS_SUBTYPE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ClinicalTrialEnrollsSubtypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'ALSSubtype'},
                        'original_optimus_relationship_type': {'equals_string': 'ENROLLS_SUBTYPE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ClinicalTrial'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ModelSystemModelsSubtypeRelationship(ALSEvidenceRelationship):
    """
    Connects a model system to the ALS subtype it models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'direct_slot': {'tag': 'direct_slot',
                                         'value': 'model_system_models_subtype'},
                         'neo4j_relationship_type': {'tag': 'neo4j_relationship_type',
                                                     'value': 'MODELS_SUBTYPE'},
                         'semantic_view_note': {'tag': 'semantic_view_note',
                                                'value': 'ALS-KG extension '
                                                         'relationship proposed for '
                                                         'Neo4j materialization; does '
                                                         'not replace current '
                                                         'OptimusKG relationships.'}},
         'class_uri': 'alskg:ModelSystemModelsSubtypeRelationship',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema',
         'slot_usage': {'object': {'name': 'object', 'range': 'ALSSubtype'},
                        'original_optimus_relationship_type': {'equals_string': 'MODELS_SUBTYPE',
                                                               'name': 'original_optimus_relationship_type'},
                        'subject': {'name': 'subject', 'range': 'ModelSystem'}}})

    has_evidence_record: Optional[list[str]] = Field(default=None, description="""Connects a relationship or semantic statement to structured supporting evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipAssertion'], 'slot_uri': 'biolink:has_evidence'} })


class ALSKGExtensionGraph(AnalyticalEntity):
    """
    Optional container class representing ALS-specific nodes and relationships added on top of an OptimusKG Neo4j graph.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskg:ALSKGExtensionGraph',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Disease',
                       'Drug',
                       'Phenotype',
                       'OntologyMetadata',
                       'EvidenceRecord',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'EvidenceStatement',
                       'Cohort',
                       'Assay',
                       'ALSKGExtensionGraph'],
         'slot_uri': 'dcterms:description'} })
    original_optimus_label: Optional[str] = Field(default=None, description="""Original three-letter OptimusKG node label as stored in Neo4j, such as GEN, DIS, or DRG.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype']} })
    direct_sources: Optional[list[str]] = Field(default=None, description="""Direct provenance sources contributing the node or edge, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })
    indirect_sources: Optional[list[str]] = Field(default=None, description="""Indirect upstream sources referenced by contributing resources, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'GeneExpressionContext']} })


class ExternalKnowledgeReference(ProvenanceEntity):
    """
    A reference to an entity, assertion, or record in an external knowledge graph or database, such as OptimusKG, PrimeKG, Open Targets, or a source dataset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'alskg:ExternalKnowledgeReference',
         'from_schema': 'https://w3id.org/alskg/schema/alskg-schema'})

    id: str = Field(default=..., description="""Primary OptimusKG node identifier, usually a CURIE or source-specific accession.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DatabaseAccession',
                       'DataSource',
                       'Publication',
                       'EvidenceRecord',
                       'Synonym',
                       'GeneExpressionContext',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'PathogenesisStatement',
                       'DifferentialExpressionStatement',
                       'ProteinAbundanceResult',
                       'PhenotypeObservation',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'DrugRepurposingHypothesis',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable preferred name or label, when available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity',
                       'OntologyClass',
                       'ClinicalEntity',
                       'PhysicalEntity',
                       'Anatomy',
                       'BiologicalProcess',
                       'CellularComponent',
                       'Disease',
                       'Drug',
                       'Exposure',
                       'Gene',
                       'MolecularFunction',
                       'Phenotype',
                       'Pathway',
                       'MolecularSubtype',
                       'OntologyMetadata',
                       'Protein',
                       'ProteinIsoform',
                       'DataSource',
                       'Publication',
                       'Synonym',
                       'AmyotrophicLateralSclerosis',
                       'DiseaseSubtype',
                       'ALSSubtype',
                       'SubtypeScheme',
                       'SubtypeCriterion',
                       'SequenceVariant',
                       'CellType',
                       'PathogenicMechanism',
                       'MolecularEvent',
                       'ProteinAggregate',
                       'EvidenceStatement',
                       'DiseaseStage',
                       'ProgressionPattern',
                       'Biomarker',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'Assay',
                       'ModelSystem',
                       'TherapeuticIntervention',
                       'ClinicalTrial',
                       'ALSKGExtensionGraph',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'rdfs:label'} })
    from_data_source: Optional[str] = Field(default=None, description="""Connects an accession, evidence item, or assertion to the source database that provided it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DatabaseAccession',
                       'EvidenceRecord',
                       'Synonym',
                       'SubtypeScheme',
                       'Study',
                       'Dataset',
                       'Cohort',
                       'Sample',
                       'ExternalKnowledgeReference'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    url: Optional[str] = Field(default=None, description="""A resolvable URL for a source, publication, evidence record, or web resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSource', 'Publication', 'ExternalKnowledgeReference'],
         'slot_uri': 'schema:url'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedEntity.model_rebuild()
OntologyClass.model_rebuild()
ClinicalEntity.model_rebuild()
PhysicalEntity.model_rebuild()
AnalyticalEntity.model_rebuild()
Anatomy.model_rebuild()
BiologicalProcess.model_rebuild()
CellularComponent.model_rebuild()
Disease.model_rebuild()
Drug.model_rebuild()
Exposure.model_rebuild()
Gene.model_rebuild()
MolecularFunction.model_rebuild()
Phenotype.model_rebuild()
Pathway.model_rebuild()
RelationshipAssertion.model_rebuild()
HierarchyRelationship.model_rebuild()
AssociationRelationship.model_rebuild()
FunctionalAnnotationRelationship.model_rebuild()
PharmacologicalRelationship.model_rebuild()
ExposureEntityRelationship.model_rebuild()
PhenotypeHierarchyRelationship.model_rebuild()
MolecularSubtypeRelationship.model_rebuild()
AnatomyGeneExpressionRelationship.model_rebuild()
DiseasePhenotypeRelationship.model_rebuild()
DrugBiologicalProcessTherapeuticRelationship.model_rebuild()
DrugDiseaseTherapeuticRelationship.model_rebuild()
DrugPhenotypeTherapeuticRelationship.model_rebuild()
DrugDrugRelationship.model_rebuild()
DrugGeneRelationship.model_rebuild()
DrugGeneTargetingRelationship.model_rebuild()
DrugGeneModulationRelationship.model_rebuild()
DrugGeneRoleRelationship.model_rebuild()
AnatomyHasParentAnatomyRelationship.model_rebuild()
AnatomyHasGeneExpressionAbsentRelationship.model_rebuild()
AnatomyHasGeneExpressionPresentRelationship.model_rebuild()
BiologicalProcessIsSubclassOfRelationship.model_rebuild()
BiologicalProcessHasParticipatingGeneRelationship.model_rebuild()
CellularComponentIsSubclassOfRelationship.model_rebuild()
CellularComponentHasLocatedGeneRelationship.model_rebuild()
DiseaseHasParentDiseaseRelationship.model_rebuild()
DiseaseAssociatedWithGeneRelationship.model_rebuild()
DiseaseHasPhenotypeRelationship.model_rebuild()
DrugHasIndicationForBiologicalProcessRelationship.model_rebuild()
DrugContraindicatedForDiseaseRelationship.model_rebuild()
DrugIndicatedForDiseaseRelationship.model_rebuild()
DrugUsedOffLabelForDiseaseRelationship.model_rebuild()
DrugHasParentDrugRelationship.model_rebuild()
DrugHasSynergisticInteractionWithDrugRelationship.model_rebuild()
DrugActivatesGeneProductRelationship.model_rebuild()
DrugAgonistOfGeneProductRelationship.model_rebuild()
DrugAllostericAntagonistOfGeneProductRelationship.model_rebuild()
DrugAntagonistOfGeneProductRelationship.model_rebuild()
DrugBindsGeneProductRelationship.model_rebuild()
DrugBlocksGeneProductRelationship.model_rebuild()
DrugHasCarrierGeneProductRelationship.model_rebuild()
DrugDegradesGeneProductRelationship.model_rebuild()
DrugHasMetabolizingEnzymeGeneProductRelationship.model_rebuild()
DrugInhibitsGeneProductRelationship.model_rebuild()
DrugInverseAgonistOfGeneProductRelationship.model_rebuild()
DrugModulatesGeneProductRelationship.model_rebuild()
DrugNegativeAllostericModulatorOfGeneProductRelationship.model_rebuild()
DrugNegativelyModulatesGeneProductRelationship.model_rebuild()
DrugOpensGeneProductRelationship.model_rebuild()
DrugPartialAgonistOfGeneProductRelationship.model_rebuild()
DrugPositiveAllostericModulatorOfGeneProductRelationship.model_rebuild()
DrugPositivelyModulatesGeneProductRelationship.model_rebuild()
DrugReleasingAgentOfGeneProductRelationship.model_rebuild()
DrugStabilizesGeneProductRelationship.model_rebuild()
DrugIsSubstrateOfGeneProductRelationship.model_rebuild()
DrugTargetsGeneProductRelationship.model_rebuild()
DrugHasTransporterGeneProductRelationship.model_rebuild()
DrugHasAdversePhenotypeRelationship.model_rebuild()
DrugAssociatedWithPhenotypeRelationship.model_rebuild()
DrugContraindicatedForPhenotypeRelationship.model_rebuild()
DrugIndicatedForPhenotypeRelationship.model_rebuild()
DrugUsedOffLabelForPhenotypeRelationship.model_rebuild()
ExposureAssociatedWithBiologicalProcessRelationship.model_rebuild()
ExposureAssociatedWithCellularComponentRelationship.model_rebuild()
ExposureLinkedToDiseaseRelationship.model_rebuild()
ExposureHasParentExposureRelationship.model_rebuild()
ExposureAssociatedWithGeneRelationship.model_rebuild()
ExposureAssociatedWithMolecularFunctionRelationship.model_rebuild()
GeneInteractsWithGeneRelationship.model_rebuild()
MolecularFunctionEnabledByGeneRelationship.model_rebuild()
MolecularFunctionIsSubclassOfRelationship.model_rebuild()
PhenotypeHasParentDiseaseRelationship.model_rebuild()
PhenotypeAssociatedWithGeneRelationship.model_rebuild()
PhenotypeHasParentPhenotypeRelationship.model_rebuild()
PathwayHasMemberGeneRelationship.model_rebuild()
PathwayHasParentPathwayRelationship.model_rebuild()
DiseaseHasMolecularSubtypeConcreteRelationship.model_rebuild()
MolecularSubtypeHasParentDiseaseRelationship.model_rebuild()
MolecularSubtypeMeasuredInAnatomyRelationship.model_rebuild()
ProvenanceEntity.model_rebuild()
Sources.model_rebuild()
OntologyMetadata.model_rebuild()
Protein.model_rebuild()
ProteinIsoform.model_rebuild()
DatabaseAccession.model_rebuild()
DataSource.model_rebuild()
Publication.model_rebuild()
EvidenceRecord.model_rebuild()
Synonym.model_rebuild()
CrossReference.model_rebuild()
GeneHasExpressionContextRelationship.model_rebuild()
ExpressionContextInAnatomyRelationship.model_rebuild()
ExpressionContextInMolecularSubtypeRelationship.model_rebuild()
AmyotrophicLateralSclerosis.model_rebuild()
DiseaseSubtype.model_rebuild()
ALSSubtype.model_rebuild()
MolecularSubtype.model_rebuild()
ClinicalSubtype.model_rebuild()
GeneticSubtype.model_rebuild()
PathologySubtype.model_rebuild()
ProgressionSubtype.model_rebuild()
SubtypeScheme.model_rebuild()
SubtypeCriterion.model_rebuild()
SequenceVariant.model_rebuild()
RepeatExpansion.model_rebuild()
CellType.model_rebuild()
PathogenicMechanism.model_rebuild()
MolecularEvent.model_rebuild()
ProteinAggregate.model_rebuild()
EvidenceStatement.model_rebuild()
PathogenesisStatement.model_rebuild()
DifferentialExpressionStatement.model_rebuild()
GeneExpressionContext.model_rebuild()
ProteinAbundanceResult.model_rebuild()
PhenotypeObservation.model_rebuild()
DiseaseStage.model_rebuild()
ProgressionPattern.model_rebuild()
Biomarker.model_rebuild()
Study.model_rebuild()
Dataset.model_rebuild()
Cohort.model_rebuild()
ComparatorGroup.model_rebuild()
Sample.model_rebuild()
Assay.model_rebuild()
ModelSystem.model_rebuild()
TherapeuticIntervention.model_rebuild()
ClinicalTrial.model_rebuild()
DrugRepurposingHypothesis.model_rebuild()
BiologicalAgent.model_rebuild()
ALSRelationship.model_rebuild()
ALSSubtypeRelationship.model_rebuild()
ALSPathogenesisRelationship.model_rebuild()
ALSExpressionRelationship.model_rebuild()
ALSEvidenceRelationship.model_rebuild()
ALSTherapeuticRelationship.model_rebuild()
DiseaseHasALSSubtypeRelationship.model_rebuild()
ALSSubtypeIsSubtypeOfDiseaseRelationship.model_rebuild()
ALSSubtypeHasSubtypeSchemeRelationship.model_rebuild()
ALSSubtypeHasSubtypeCriterionRelationship.model_rebuild()
ALSSubtypeDefinedByGeneRelationship.model_rebuild()
ALSSubtypeDefinedByVariantRelationship.model_rebuild()
ALSSubtypeHasPathogenicMechanismRelationship.model_rebuild()
ALSSubtypeAffectsAnatomyRelationship.model_rebuild()
ALSSubtypeInvolvesCellTypeRelationship.model_rebuild()
ALSSubtypeHasPhenotypeObservationRelationship.model_rebuild()
GeneHasVariantRelationship.model_rebuild()
VariantAffectsGeneRelationship.model_rebuild()
VariantAltersProteinRelationship.model_rebuild()
GeneContributesToPathogenicMechanismRelationship.model_rebuild()
ProteinContributesToPathogenicMechanismRelationship.model_rebuild()
MolecularEventContributesToPathogenicMechanismRelationship.model_rebuild()
PathogenicMechanismOccursInCellTypeRelationship.model_rebuild()
PathogenicMechanismOccursInAnatomyRelationship.model_rebuild()
DifferentialExpressionMeasuresGeneRelationship.model_rebuild()
DifferentialExpressionOccursInSubtypeRelationship.model_rebuild()
DifferentialExpressionOccursInAnatomyRelationship.model_rebuild()
DifferentialExpressionOccursInCellTypeRelationship.model_rebuild()
DifferentialExpressionMeasuredByAssayRelationship.model_rebuild()
DifferentialExpressionDerivedFromDatasetRelationship.model_rebuild()
EvidenceStatementSupportedByEvidenceRelationship.model_rebuild()
EvidenceStatementDerivedFromDatasetRelationship.model_rebuild()
PhenotypeObservationHasObservedPhenotypeRelationship.model_rebuild()
PhenotypeObservationOccursInSubtypeRelationship.model_rebuild()
BiomarkerIndicatesPathogenicMechanismRelationship.model_rebuild()
DrugRepurposingHypothesisPrioritizesDrugRelationship.model_rebuild()
DrugRepurposingHypothesisTargetsGeneRelationship.model_rebuild()
DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship.model_rebuild()
TherapeuticInterventionTestedInClinicalTrialRelationship.model_rebuild()
ClinicalTrialEnrollsSubtypeRelationship.model_rebuild()
ModelSystemModelsSubtypeRelationship.model_rebuild()
ALSKGExtensionGraph.model_rebuild()
ExternalKnowledgeReference.model_rebuild()
