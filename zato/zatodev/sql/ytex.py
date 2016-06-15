# coding: utf-8
from sqlalchemy import BINARY, BigInteger, Column, DateTime, Float, Index, Integer, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import BIT, LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AnnoBase(Base):
    __tablename__ = 'anno_base'
    __table_args__ = (
        Index('IX_type_span', 'document_id', 'span_begin', 'span_end', 'uima_type_id'),
        Index('IX_type', 'document_id', 'uima_type_id')
    )

    anno_base_id = Column(Integer, primary_key=True)
    document_id = Column(Integer, nullable=False, index=True)
    span_begin = Column(Integer)
    span_end = Column(Integer)
    uima_type_id = Column(Integer, nullable=False)


class AnnoBaseSequence(Base):
    __tablename__ = 'anno_base_sequence'

    sequence_name = Column(String(100), primary_key=True)
    next_val = Column(Integer, nullable=False, server_default=text("'1'"))


class AnnoContain(Base):
    __tablename__ = 'anno_contain'
    __table_args__ = (
        Index('IX_parent_id_child_type', 'parent_anno_base_id', 'child_uima_type_id'),
        Index('IX_child_id_parent_type', 'child_anno_base_id', 'parent_uima_type_id')
    )

    parent_anno_base_id = Column(Integer, primary_key=True, nullable=False)
    parent_uima_type_id = Column(Integer, nullable=False)
    child_anno_base_id = Column(Integer, primary_key=True, nullable=False)
    child_uima_type_id = Column(Integer, nullable=False)


class AnnoDate(Base):
    __tablename__ = 'anno_date'

    anno_base_id = Column(Integer, primary_key=True)
    tstamp = Column(DateTime)


class AnnoLink(Base):
    __tablename__ = 'anno_link'
    __table_args__ = (
        Index('IX_link', 'parent_anno_base_id', 'child_anno_base_id', 'feature'),
    )

    anno_link_id = Column(Integer, primary_key=True)
    parent_anno_base_id = Column(Integer, nullable=False)
    child_anno_base_id = Column(Integer, nullable=False)
    feature = Column(String(20))


class AnnoMarkable(Base):
    __tablename__ = 'anno_markable'

    anno_base_id = Column(Integer, primary_key=True)
    id = Column(Integer, server_default=text("'0'"))
    anaphoric_prob = Column(Float(asdecimal=True), server_default=text("'0'"))
    content = Column(Integer, server_default=text("'0'"))


class AnnoMedEvent(Base):
    __tablename__ = 'anno_med_event'

    anno_base_id = Column(Integer, primary_key=True)
    discoveryTechnique = Column(Integer)
    status = Column(Integer)
    polarity = Column(Integer)
    uncertainty = Column(Integer)
    conditional = Column(BIT(1))
    generic = Column(BIT(1))
    typeID = Column(Integer)
    confidence = Column(Float)
    segmentID = Column(String(20))
    freqNumber = Column(String(10))
    freqUnit = Column(String(10))
    strengthNumber = Column(String(10))
    strengthUnit = Column(String(10))
    change = Column(String(10))
    dosage = Column(String(10))


class AnnoMmAcronym(Base):
    __tablename__ = 'anno_mm_acronym'

    anno_base_id = Column(Integer, primary_key=True)
    acronym = Column(String(10))
    expansion = Column(String(30))


class AnnoMmCandidate(Base):
    __tablename__ = 'anno_mm_candidate'

    anno_base_id = Column(Integer, primary_key=True)
    cui = Column(String(8))
    score = Column(Integer, server_default=text("'0'"))
    head = Column(BIT(1))
    overmatch = Column(BIT(1))


class AnnoMmCuiconcept(Base):
    __tablename__ = 'anno_mm_cuiconcept'

    anno_mm_cuiconcept_id = Column(Integer, primary_key=True)
    anno_base_id = Column(Integer)
    negExCui = Column(String(8))


class AnnoMmNegation(Base):
    __tablename__ = 'anno_mm_negation'

    anno_base_id = Column(Integer, primary_key=True)
    negType = Column(String(10))
    negTrigger = Column(String(10))


class AnnoMmUtterance(Base):
    __tablename__ = 'anno_mm_utterance'

    anno_base_id = Column(Integer, primary_key=True)
    pmid = Column(String(10))
    location = Column(String(30))


class AnnoNamedEntity(Base):
    __tablename__ = 'anno_named_entity'

    anno_base_id = Column(Integer, primary_key=True)
    discoveryTechnique = Column(Integer)
    status = Column(Integer)
    polarity = Column(Integer)
    uncertainty = Column(Integer)
    conditional = Column(BIT(1))
    generic = Column(BIT(1))
    typeID = Column(Integer)
    confidence = Column(Float)
    segmentID = Column(String(20))


class AnnoOntologyConcept(Base):
    __tablename__ = 'anno_ontology_concept'
    __table_args__ = (
        Index('IX_anno_cui', 'anno_base_id', 'cui'),
        Index('IX_anno_code', 'anno_base_id', 'code')
    )

    anno_ontology_concept_id = Column(Integer, primary_key=True)
    anno_base_id = Column(Integer, nullable=False, index=True)
    code = Column(String(20), index=True)
    cui = Column(String(8))
    disambiguated = Column(BIT(1), nullable=False)


class AnnoSegment(Base):
    __tablename__ = 'anno_segment'
    __table_args__ = (
        Index('IX_segment_anno_seg', 'anno_base_id', 'id'),
    )

    anno_base_id = Column(Integer, primary_key=True)
    id = Column(String(20))


class AnnoSentence(Base):
    __tablename__ = 'anno_sentence'

    anno_base_id = Column(Integer, primary_key=True)
    sentenceNumber = Column(Integer)
    segmentId = Column(String(20))


class AnnoToken(Base):
    __tablename__ = 'anno_token'

    anno_base_id = Column(Integer, primary_key=True)
    tokenNumber = Column(Integer, nullable=False, server_default=text("'0'"))
    normalizedForm = Column(String(20))
    partofSpeech = Column(String(5))
    coveredText = Column(String(20), index=True)
    capitalization = Column(Integer, nullable=False, server_default=text("'0'"))
    numPosition = Column(Integer, nullable=False, server_default=text("'0'"))
    suggestion = Column(String(20))
    canonicalForm = Column(String(20), index=True)
    negated = Column(BIT(1), nullable=False)
    possible = Column(BIT(1), nullable=False)


class AnnoTreebankNode(Base):
    __tablename__ = 'anno_treebank_node'

    anno_base_id = Column(Integer, primary_key=True)
    parent = Column(Integer, server_default=text("'0'"))
    nodeType = Column(String(10))
    nodeValue = Column(String(10))
    leaf = Column(BIT(1))
    headIndex = Column(Integer, server_default=text("'0'"))
    index = Column(Integer, server_default=text("'0'"))
    tokenIndex = Column(Integer, server_default=text("'0'"))


class ClassifierEval(Base):
    __tablename__ = 'classifier_eval'

    classifier_eval_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    experiment = Column(String(50), server_default=text("''"))
    fold = Column(Integer)
    run = Column(Integer)
    algorithm = Column(String(50), server_default=text("''"))
    label = Column(String(50), server_default=text("''"))
    options = Column(String(1000), server_default=text("''"))
    model = Column(LONGBLOB)
    param1 = Column(Float(asdecimal=True))
    param2 = Column(String(50))


class ClassifierEvalIr(Base):
    __tablename__ = 'classifier_eval_ir'
    __table_args__ = (
        Index('NK_classifier_eval_ircls', 'classifier_eval_id', 'ir_type', 'ir_class', unique=True),
    )

    classifier_eval_ir_id = Column(Integer, primary_key=True)
    classifier_eval_id = Column(Integer, nullable=False, index=True)
    ir_type = Column(String(5), nullable=False, server_default=text("''"))
    ir_class = Column(String(5), nullable=False, server_default=text("''"))
    ir_class_id = Column(Integer)
    tp = Column(Integer, nullable=False)
    tn = Column(Integer, nullable=False)
    fp = Column(Integer, nullable=False)
    fn = Column(Integer, nullable=False)
    ppv = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    npv = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    sens = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    spec = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    f1 = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))


class ClassifierEvalSemil(Base):
    __tablename__ = 'classifier_eval_semil'

    classifier_eval_id = Column(Integer, primary_key=True)
    distance = Column(String(50))
    degree = Column(Integer, nullable=False, server_default=text("'0'"))
    gamma = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    soft_label = Column(BIT(1), nullable=False)
    norm_laplace = Column(BIT(1), nullable=False)
    mu = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    _lambda = Column('lambda', Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    pct_labeled = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))


class ClassifierEvalSvm(Base):
    __tablename__ = 'classifier_eval_svm'

    classifier_eval_id = Column(Integer, primary_key=True)
    cost = Column(Float(asdecimal=True), server_default=text("'0'"))
    weight = Column(String(50))
    degree = Column(Integer, server_default=text("'0'"))
    gamma = Column(Float(asdecimal=True), server_default=text("'0'"))
    kernel = Column(Integer)
    supportVectors = Column(Integer)
    vcdim = Column(Float(asdecimal=True))


class ClassifierInstanceEval(Base):
    __tablename__ = 'classifier_instance_eval'
    __table_args__ = (
        Index('nk_result', 'classifier_eval_id', 'instance_id', unique=True),
    )

    classifier_instance_eval_id = Column(Integer, primary_key=True)
    classifier_eval_id = Column(Integer, nullable=False)
    instance_id = Column(BigInteger, nullable=False)
    pred_class_id = Column(Integer, nullable=False)
    target_class_id = Column(Integer)


class ClassifierInstanceEvalProb(Base):
    __tablename__ = 'classifier_instance_eval_prob'
    __table_args__ = (
        Index('nk_result_prob', 'classifier_instance_eval_id', 'class_id', unique=True),
    )

    classifier_eval_result_prob_id = Column(Integer, primary_key=True)
    classifier_instance_eval_id = Column(Integer)
    class_id = Column(Integer, nullable=False)
    probability = Column(Float(asdecimal=True), nullable=False)


class CorpusDoc(Base):
    __tablename__ = 'corpus_doc'
    __table_args__ = (
        Index('IX_doc_group', 'corpus_name', 'doc_group'),
    )

    corpus_name = Column(String(50), primary_key=True, nullable=False)
    instance_id = Column(BigInteger, primary_key=True, nullable=False)
    doc_text = Column(String)
    doc_group = Column(String(50))


class CorpusLabel(Base):
    __tablename__ = 'corpus_label'
    __table_args__ = (
        Index('FK_corpus_doc', 'corpus_name', 'instance_id'),
    )

    corpus_name = Column(String(50), primary_key=True, nullable=False)
    instance_id = Column(BigInteger, primary_key=True, nullable=False)
    label = Column(String(20), primary_key=True, nullable=False, server_default=text("''"))
    _class = Column('class', String(5), nullable=False, server_default=text("''"))


class CvBestSvm(Base):
    __tablename__ = 'cv_best_svm'

    corpus_name = Column(String(50), primary_key=True, nullable=False)
    label = Column(String(50), primary_key=True, nullable=False)
    experiment = Column(String(50), primary_key=True, nullable=False, server_default=text("''"))
    f1 = Column(Float(asdecimal=True))
    kernel = Column(Integer)
    cost = Column(Float(asdecimal=True))
    weight = Column(String(50))
    param1 = Column(Float(asdecimal=True))
    param2 = Column(String(50))


class CvFold(Base):
    __tablename__ = 'cv_fold'
    __table_args__ = (
        Index('nk_cv_fold', 'corpus_name', 'split_name', 'label', 'run', 'fold', unique=True),
    )

    cv_fold_id = Column(Integer, primary_key=True)
    corpus_name = Column(String(50), nullable=False)
    split_name = Column(String(50), nullable=False, server_default=text("''"))
    label = Column(String(50), nullable=False, server_default=text("''"))
    run = Column(Integer, nullable=False, server_default=text("'0'"))
    fold = Column(Integer, nullable=False, server_default=text("'0'"))


class CvFoldInstance(Base):
    __tablename__ = 'cv_fold_instance'
    __table_args__ = (
        Index('nk_cv_fold_instance', 'cv_fold_id', 'instance_id', 'train', unique=True),
    )

    cv_fold_instance_id = Column(Integer, primary_key=True)
    cv_fold_id = Column(Integer, nullable=False)
    instance_id = Column(BigInteger, nullable=False)
    train = Column(BIT(1), nullable=False)


class Document(Base):
    __tablename__ = 'document'
    __table_args__ = (
        Index('IX_document_analysis_batch', 'analysis_batch', 'document_id'),
    )

    document_id = Column(Integer, primary_key=True)
    instance_id = Column(BigInteger, nullable=False, index=True, server_default=text("'0'"))
    instance_key = Column(String(256), index=True)
    analysis_batch = Column(String(50), nullable=False)
    cas = Column(LONGBLOB)
    doc_text = Column(Text)


class FeatureEval(Base):
    __tablename__ = 'feature_eval'
    __table_args__ = (
        Index('nk_feature_eval', 'corpus_name', 'featureset_name', 'label', 'cv_fold_id', 'param1', 'param2', 'type', unique=True),
        Index('ix_feature_eval', 'corpus_name', 'cv_fold_id', 'type')
    )

    feature_eval_id = Column(Integer, primary_key=True)
    corpus_name = Column(String(50), nullable=False)
    featureset_name = Column(String(50), nullable=False, server_default=text("''"))
    label = Column(String(50), nullable=False, server_default=text("''"))
    cv_fold_id = Column(Integer, nullable=False, server_default=text("'0'"))
    param1 = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    param2 = Column(String(50), nullable=False, server_default=text("''"))
    type = Column(String(50), nullable=False)


class FeatureParchd(Base):
    __tablename__ = 'feature_parchd'
    __table_args__ = (
        Index('NK_feature_parent', 'par_feature_rank_id', 'chd_feature_rank_id', unique=True),
    )

    feature_parchd_id = Column(Integer, primary_key=True)
    par_feature_rank_id = Column(Integer, nullable=False)
    chd_feature_rank_id = Column(Integer, nullable=False)


class FeatureRank(Base):
    __tablename__ = 'feature_rank'
    __table_args__ = (
        Index('ix_feature_rank', 'feature_eval_id', 'rank'),
        Index('nk_feature_name', 'feature_eval_id', 'feature_name', unique=True),
        Index('ix_feature_evaluation', 'feature_eval_id', 'evaluation')
    )

    feature_rank_id = Column(Integer, primary_key=True)
    feature_eval_id = Column(Integer, nullable=False, index=True)
    feature_name = Column(String(50), nullable=False)
    evaluation = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    rank = Column(Integer, nullable=False, server_default=text("'0'"))


class FractureDemo(Base):
    __tablename__ = 'fracture_demo'

    note_id = Column(Integer, primary_key=True)
    site_id = Column(String(10))
    note_text = Column(Text)
    fracture = Column(String(20))
    note_set = Column(String(10))


class HibernateSequences(Base):
    __tablename__ = 'hibernate_sequences'

    sequence_name = Column(String(100), primary_key=True)
    next_val = Column(Integer, nullable=False, server_default=text("'1'"))


class Hotspot(Base):
    __tablename__ = 'hotspot'
    __table_args__ = (
        Index('NK_hotspot', 'instance_id', 'anno_base_id', 'feature_rank_id', unique=True),
    )

    hotspot_id = Column(Integer, primary_key=True)
    instance_id = Column(Integer, nullable=False, index=True)
    anno_base_id = Column(Integer, nullable=False, index=True)
    feature_rank_id = Column(Integer, nullable=False, index=True)


class HotspotInstance(Base):
    __tablename__ = 'hotspot_instance'
    __table_args__ = (
        Index('NK_hotspot_instance', 'corpus_name', 'experiment', 'label', 'instance_id', unique=True),
    )

    hotspot_instance_id = Column(Integer, primary_key=True)
    corpus_name = Column(String(50), nullable=False)
    experiment = Column(String(50), nullable=False, server_default=text("''"))
    label = Column(String(50), nullable=False, server_default=text("''"))
    instance_id = Column(Integer, nullable=False)
    max_evaluation = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    min_rank = Column(Integer, nullable=False, server_default=text("'0'"))


class HotspotSentence(Base):
    __tablename__ = 'hotspot_sentence'
    __table_args__ = (
        Index('IX_evaluation', 'hotspot_instance_id', 'evaluation'),
        Index('NK_hotspot_sentence', 'hotspot_instance_id', 'anno_base_id', unique=True),
        Index('IX_rank', 'hotspot_instance_id', 'rank')
    )

    hotspot_sentence_id = Column(Integer, primary_key=True)
    hotspot_instance_id = Column(Integer, nullable=False, index=True)
    anno_base_id = Column(Integer, nullable=False, index=True)
    evaluation = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    rank = Column(Integer, nullable=False, server_default=text("'0'"))


class KernelEval(Base):
    __tablename__ = 'kernel_eval'
    __table_args__ = (
        Index('NK_kernel_eval', 'corpus_name', 'experiment', 'label', 'cv_fold_id', 'param1', 'param2', unique=True),
    )

    kernel_eval_id = Column(Integer, primary_key=True)
    corpus_name = Column(String(50), nullable=False, server_default=text("''"))
    experiment = Column(String(50), nullable=False)
    label = Column(String(50), nullable=False, server_default=text("''"))
    cv_fold_id = Column(Integer, nullable=False, server_default=text("'0'"))
    param1 = Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
    param2 = Column(String(50), nullable=False, server_default=text("''"))


class KernelEvalInstance(Base):
    __tablename__ = 'kernel_eval_instance'
    __table_args__ = (
        Index('NK_kernel_eval', 'kernel_eval_id', 'instance_id1', 'instance_id2', unique=True),
        Index('IX_kernel_eval1', 'kernel_eval_id', 'instance_id1'),
        Index('IX_kernel_eval2', 'kernel_eval_id', 'instance_id2')
    )

    kernel_eval_instance = Column(Integer, primary_key=True)
    kernel_eval_id = Column(Integer, nullable=False)
    instance_id1 = Column(BigInteger, nullable=False)
    instance_id2 = Column(BigInteger, nullable=False)
    similarity = Column(Float(asdecimal=True), nullable=False)


class RefNamedEntityRegex(Base):
    __tablename__ = 'ref_named_entity_regex'

    named_entity_regex_id = Column(Integer, primary_key=True)
    regex = Column(String(512), nullable=False)
    coding_scheme = Column(String(20), nullable=False)
    code = Column(String(20), nullable=False)
    oid = Column(String(10))
    context = Column(String(256))


class RefSegmentRegex(Base):
    __tablename__ = 'ref_segment_regex'

    segment_regex_id = Column(Integer, primary_key=True)
    regex = Column(String(256), nullable=False)
    segment_id = Column(String(20))
    limit_to_regex = Column(BIT(1))


class RefStopword(Base):
    __tablename__ = 'ref_stopword'

    stopword = Column(String(50), primary_key=True)


class RefUimaType(Base):
    __tablename__ = 'ref_uima_type'

    uima_type_id = Column(Integer, primary_key=True)
    uima_type_name = Column(String(256), nullable=False, unique=True)
    table_name = Column(String(100))


class TfidfDoclength(Base):
    __tablename__ = 'tfidf_doclength'
    __table_args__ = (
        Index('nk_instance_id', 'feature_eval_id', 'instance_id', unique=True),
    )

    tfidf_doclength_id = Column(Integer, primary_key=True)
    feature_eval_id = Column(Integer, nullable=False)
    instance_id = Column(BigInteger, nullable=False)
    length = Column(Integer, nullable=False, server_default=text("'0'"))


class UmlsAuiFword(Base):
    __tablename__ = 'umls_aui_fword'

    aui = Column(String(10), primary_key=True)
    fword = Column(String(70), nullable=False, index=True)
    fstem = Column(String(70), index=True)
    tok_str = Column(String(250), nullable=False)
    stem_str = Column(String(250))


t_v_annotation = Table(
    'v_annotation', metadata,
    Column('anno_base_id', Integer),
    Column('document_id', Integer),
    Column('span_begin', Integer),
    Column('span_end', Integer),
    Column('uima_type_id', Integer),
    Column('uima_type_name', String(256)),
    Column('anno_text', String),
    Column('analysis_batch', String(50))
)


t_v_corpus_group_class = Table(
    'v_corpus_group_class', metadata,
    Column('corpus_name', String(50)),
    Column('label', String(20)),
    Column('doc_group', String(50)),
    Column('class', String(5))
)


t_v_document = Table(
    'v_document', metadata,
    Column('analysis_batch', String(50)),
    Column('document_id', Integer),
    Column('doc_text', Text),
    Column('instance_id', BigInteger, server_default=text("'0'")),
    Column('patient_id', BINARY(0)),
    Column('doc_date', BINARY(0)),
    Column('doc_title', BINARY(0)),
    Column('document_type_name', BINARY(0))
)


t_v_document_cui_sent = Table(
    'v_document_cui_sent', metadata,
    Column('anno_base_id', Integer),
    Column('analysis_batch', String(50)),
    Column('document_id', Integer),
    Column('polarity', Integer),
    Column('code', String(20)),
    Column('cui', String(8)),
    Column('cui_text', String),
    Column('sentence_text', String),
    Column('disambiguated', BIT(1), server_default=text("'b''0'''")),
    Column('patient_id', BINARY(0)),
    Column('doc_date', BINARY(0)),
    Column('doc_title', BINARY(0)),
    Column('document_type_name', BINARY(0))
)


t_v_document_ontoanno = Table(
    'v_document_ontoanno', metadata,
    Column('document_id', Integer),
    Column('span_begin', Integer),
    Column('span_end', Integer),
    Column('polarity', Integer),
    Column('code', String(20)),
    Column('cui', String(8)),
    Column('analysis_batch', String(50)),
    Column('disambiguated', BIT(1), server_default=text("'b''0'''"))
)


t_v_snomed_fword_lookup = Table(
    'v_snomed_fword_lookup', metadata,
    Column('cui', String(8), nullable=False, index=True),
    Column('tui', String(8)),
    Column('fword', String(70), nullable=False, index=True),
    Column('fstem', String(70), index=True),
    Column('tok_str', String(250), nullable=False),
    Column('stem_str', String(250))
)
