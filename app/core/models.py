from django.db import models


class ExcelFile(models.Model):
    file_name = models.FileField(upload_to='uploads')
    date_created = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    
    def __str__(self):
        return f'File Id{self.id} File name {self.file_name}'

class CsvFile(models.Model):
    file_name = models.FileField(upload_to='uploads')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    
    def __str__(self):
        return f'File Id{self.id} File name {self.file_name}'

class Laboratorio(models.Model):
    patient_id = models.IntegerField()
    nome = models.CharField(max_length=255, blank=True, null=True)
    nid = models.CharField(max_length=255, blank=True, null=True)
    sexo = models.CharField(max_length=2, blank=True, null=True)
    us_name = models.CharField(max_length=255, blank=True, null=True)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_pedido = models.DateTimeField(null=True, blank=True)
    data_colheita = models.DateTimeField(null=True, blank=True)
    data_resultado = models.DateTimeField(null=True, blank=True)
    WBC = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    RBC = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    HGB_HB = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    HCT_PCV = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    HCV_VCM_VGM = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    MCH_HGM_HCM = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    MCHC_CHCM_CMHG = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PLT = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    RDW = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    VS_VHS = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    MPV = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Tipagem_Sanguinea = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    LYM_Percentual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    LYM_Absoluto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    NEUT_Percentual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    NEUT_Absoluto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Eosinofilo_Percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Eosinofilo_Abs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Basofilo_Percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Basofilo_Abs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Monocito_Percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Monocito_Abs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    VDRL = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    RPR = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cd4_absoluto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cd4_percentual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_carga = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    qualidade_carga = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    GeneXpert = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    MTBdetectado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nivelMTBdetectado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Rifamoin = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Cultura = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    TB_LAM = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    CRAG = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    baciloscopia = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    NivelPositividade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ALB = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    AST_SGOT_GOT = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ALT_SGT_GPT = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    AMI = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    BIL = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    COL = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    HDL = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    LDL = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Cr = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    CK_CPK = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Fosfatase_Alcalina = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    GGT = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    GLC = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    LDH = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Lactato = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Lipase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Total_Proteina = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    TG = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Ureia = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Cloreto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Potassio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Sodio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Globulinas = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PCR = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f'{self.nome} {self.data_pedido}'
    

    
