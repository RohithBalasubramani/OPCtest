from django.db import models

class BaseReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

# HT Feeders
class HTFeederReading(BaseReading):
    app_energy_export = models.FloatField()
    avg_ac_power = models.FloatField()
    avg_app_power = models.FloatField()
    avg_current = models.FloatField()
    avg_pf = models.FloatField()
    avg_rac_power = models.FloatField()
    avg_voltage = models.FloatField()
    b_ac_power = models.FloatField()
    b_app_power = models.FloatField()
    b_current = models.FloatField()
    b_pf = models.FloatField()
    b_rac_power = models.FloatField()
    b_voltage = models.FloatField()
    br_voltage = models.FloatField()
    frequency = models.FloatField()
    pn_voltage = models.FloatField()
    r_ac_power = models.FloatField()
    r_app_power = models.FloatField()
    r_current = models.FloatField()
    r_pf = models.FloatField()
    r_rac_power = models.FloatField()
    r_voltage = models.FloatField()
    ry_voltage = models.FloatField()
    thd_voltage_an = models.FloatField()
    thd_voltage_cn = models.FloatField()
    thd_voltage_en = models.FloatField()
    today_app_energy_export = models.FloatField()
    today_export = models.FloatField()
    today_import = models.FloatField()
    total_export = models.FloatField()
    total_import = models.FloatField()
    y_ac_power = models.FloatField()
    y_app_power = models.FloatField()
    y_current = models.FloatField()
    y_pf = models.FloatField()
    y_rac_power = models.FloatField()
    y_voltage = models.FloatField()
    yb_voltage = models.FloatField()
    yes_app_energy_export = models.FloatField()
    yes_export = models.FloatField()
    yes_import = models.FloatField()

    class Meta:
        abstract = True  # Make the model abstract

# LT Panels and Transformers
class LTPanelReading(BaseReading):
    app_energy = models.FloatField()
    avg_current = models.FloatField()
    avg_line_voltage = models.FloatField()
    avg_phase_voltage = models.FloatField()
    avg_power_factor = models.FloatField()
    b_active_power = models.FloatField()
    b_app_power = models.FloatField()
    b_current = models.FloatField()
    b_phase_voltage = models.FloatField()
    b_reactive_power = models.FloatField()
    br_voltage = models.FloatField()
    frequency = models.FloatField()
    r_active_power = models.FloatField()
    r_app_power = models.FloatField()
    r_current = models.FloatField()
    r_phase_voltage = models.FloatField()
    r_reactive_power = models.FloatField()
    ry_voltage = models.FloatField()
    today_app_energy = models.FloatField()
    today_export = models.FloatField()
    today_import = models.FloatField()
    total_energy_export = models.FloatField()
    total_energy_import = models.FloatField()
    total_reactive_power = models.FloatField()
    y_active_power = models.FloatField()
    y_app_power = models.FloatField()
    y_current = models.FloatField()
    y_current_demo = models.FloatField()
    y_phase_voltage = models.FloatField()
    y_power_factor = models.FloatField()
    y_reactive_power = models.FloatField()
    yb_voltage = models.FloatField()

    class Meta:
        abstract = True  # Make the model abstract

# Inverters
class InverterReading(BaseReading):
    ac_power = models.FloatField()
    b_ac_power = models.FloatField()
    b_current = models.FloatField()
    b_voltage = models.FloatField()
    br_voltage = models.FloatField()
    dc_current = models.FloatField()
    dc_power = models.FloatField()
    dc_voltage = models.FloatField()
    efficiency = models.FloatField()
    fault = models.CharField(max_length=255)  # Assuming 'Word' means a string field
    frequency = models.FloatField()
    inv_fault_subcode = models.CharField(max_length=255)  # Assuming 'Word' means a string field
    inv_warning_bit_h = models.IntegerField()  # Assuming 'Bit' means an integer field
    inv_warning_subcode = models.IntegerField()  # Assuming 'Bit' means an integer field
    peak_power = models.FloatField()
    pf = models.FloatField()
    pv1_current = models.FloatField()
    pv1_dc_current = models.FloatField()
    pv1_dc_power = models.FloatField()
    pv1_dc_voltage = models.FloatField()
    pv1_voltage = models.FloatField()
    pv10_current = models.FloatField()
    pv10_voltage = models.FloatField()
    pv11_current = models.FloatField()
    pv11_voltage = models.FloatField()
    pv12_current = models.FloatField()
    pv12_voltage = models.FloatField()
    pv13_current = models.FloatField()
    pv13_voltage = models.FloatField()
    pv14_current = models.FloatField()
    pv14_voltage = models.FloatField()
    pv15_current = models.FloatField()
    pv15_voltage = models.FloatField()
    pv16_current = models.FloatField()
    pv16_voltage = models.FloatField()
    pv17_current = models.FloatField()
    pv17_voltage = models.FloatField()
    pv18_current = models.FloatField()
    pv18_voltage = models.FloatField()
    pv19_current = models.FloatField()
    pv19_voltage = models.FloatField()
    pv2_current = models.FloatField()
    pv2_dc_current = models.FloatField()
    pv2_dc_power = models.FloatField()
    pv2_dc_voltage = models.FloatField()
    pv2_voltage = models.FloatField()
    pv20_current = models.FloatField()
    pv20_voltage = models.FloatField()
    pv3_current = models.FloatField()
    pv3_dc_current = models.FloatField()
    pv3_dc_power = models.FloatField()
    pv3_dc_voltage = models.FloatField()
    pv3_voltage = models.FloatField()
    pv4_current = models.FloatField()
    pv4_dc_current = models.FloatField()
    pv4_dc_power = models.FloatField()
    pv4_dc_voltage = models.FloatField()
    pv4_voltage = models.FloatField()
    pv5_current = models.FloatField()
    pv5_dc_current = models.FloatField()
    pv5_dc_power = models.FloatField()
    pv5_dc_voltage = models.FloatField()
    pv5_voltage = models.FloatField()
    pv6_current = models.FloatField()
    pv6_dc_current = models.FloatField()
    pv6_dc_power = models.FloatField()
    pv6_dc_voltage = models.FloatField()
    pv6_voltage = models.FloatField()
    pv7_current = models.FloatField()
    pv7_dc_current = models.FloatField()
    pv7_dc_power = models.FloatField()
    pv7_dc_voltage = models.FloatField()
    pv7_voltage = models.FloatField()
    pv8_current = models.FloatField()
    pv8_dc_current = models.FloatField()
    pv8_dc_power = models.FloatField()
    pv8_dc_voltage = models.FloatField()
    pv8_voltage = models.FloatField()
    pv9_current = models.FloatField()
    pv9_voltage = models.FloatField()
    r_ac_power = models.FloatField()
    r_current = models.FloatField()
    r_voltage = models.FloatField()
    ry_voltage = models.FloatField()
    status = models.CharField(max_length=255)  # Assuming 'Word' means a string field
    temp = models.FloatField()
    today_energy = models.FloatField()
    total_energy = models.FloatField()
    total_strings_current = models.FloatField()
    y_ac_power = models.FloatField()
    y_current = models.FloatField()
    y_voltage = models.FloatField()
    yb_voltage = models.FloatField()
    yest_energy = models.FloatField()

    class Meta:
        abstract = True  # Make the model abstract


# PEPPL HT models for Phase 1
class P1_PepplHT_HTPanelIncomer(HTFeederReading):
    pass

class P1_PepplHT_OutGoing1(HTFeederReading):
    pass

class P1_PepplHT_OutGoing2(HTFeederReading):
    pass

class P1_PepplHT_OutGoing3(HTFeederReading):
    pass

class P1_PepplHT_OutGoing4(HTFeederReading):
    pass

# AMFS models for Phase 1
class P1_AMFS_Transformer1(LTPanelReading):
    pass

class P1_AMFS_Generator1(LTPanelReading):
    pass

class P1_AMFS_Outgoing1(LTPanelReading):
    pass

class P1_AMFS_APFC1(LTPanelReading):
    pass

class P1_AMFS_Transformer2(LTPanelReading):
    pass

class P1_AMFS_Generator2(LTPanelReading):
    pass

class P1_AMFS_Outgoing2(LTPanelReading):
    pass

class P1_AMFS_APFC2(LTPanelReading):
    pass

class P1_AMFS_Transformer3(LTPanelReading):
    pass

class P1_AMFS_Generator3(LTPanelReading):
    pass

class P1_AMFS_Outgoing3(LTPanelReading):
    pass

class P1_AMFS_APFC3(LTPanelReading):
    pass

class P1_AMFS_Transformer4(LTPanelReading):
    pass

class P1_AMFS_Generator4(LTPanelReading):
    pass

class P1_AMFS_Outgoing4(LTPanelReading):
    pass

class P1_AMFS_APFC4(LTPanelReading):
    pass

# APFC Panels models for Phase 1
class P1_APFCPanels_Panel1(LTPanelReading):
    pass

class P1_APFCPanels_Panel2(LTPanelReading):
    pass

class P1_APFCPanels_Panel3(LTPanelReading):
    pass

class P1_APFCPanels_Panel4(LTPanelReading):
    pass

# PCC-1 models for Phase 1
class P1_PCC1_CellIncomer(LTPanelReading):
    pass

class P1_PCC1_UPS1A(LTPanelReading):
    pass

class P1_PCC1_UPS1B(LTPanelReading):
    pass

class P1_PCC1_UPS1C(LTPanelReading):
    pass

class P1_PCC1_UPS1D(LTPanelReading):
    pass

class P1_PCC1_UPS1E(LTPanelReading):
    pass

class P1_PCC1_LTP1(LTPanelReading):
    pass

class P1_PCC1_LTP2(LTPanelReading):
    pass

class P1_PCC1_Chiller2(LTPanelReading):
    pass

# PCC-2 models for Phase 1
class P1_PCC2_CellIncomer(LTPanelReading):
    pass

class P1_PCC2_Lighting(LTPanelReading):
    pass

class P1_PCC2_UPS2A(LTPanelReading):
    pass

class P1_PCC2_UPS2B(LTPanelReading):
    pass

class P1_PCC2_UPS2C(LTPanelReading):
    pass

class P1_PCC2_UPS2D(LTPanelReading):
    pass

class P1_PCC2_UPS2E(LTPanelReading):
    pass

class P1_PCC2_OGCellToolPDB2(LTPanelReading):
    pass

class P1_PCC2_OGCellLTP2(LTPanelReading):
    pass

# PCC-3 models for Phase 1
class P1_PCC3_CellIncomer(LTPanelReading):
    pass

class P1_PCC3_SolarIncomer(LTPanelReading):
    pass

class P1_PCC3_Chiller3(LTPanelReading):
    pass

class P1_PCC3_Chiller4(LTPanelReading):
    pass

class P1_PCC3_CellLTP3(LTPanelReading):
    pass

class P1_PCC3_MEETFP(LTPanelReading):
    pass

class P1_PCC3_ConcentratorETP(LTPanelReading):
    pass

class P1_PCC3_DIStream(LTPanelReading):
    pass

class P1_PCC3_RinseStream(LTPanelReading):
    pass

class P1_PCC3_ConcentratorStream(LTPanelReading):
    pass

class P1_PCC3_MVR(LTPanelReading):
    pass

class P1_PCC3_FireHydrant(LTPanelReading):
    pass

class P1_PCC3_DGExhaust(LTPanelReading):
    pass

class P1_PCC3_ExhaustUtility(LTPanelReading):
    pass

class P1_PCC3_ScrubberExhaust(LTPanelReading):
    pass

# PCC-4 models for Phase 1
class P1_PCC4_CellIncomer(LTPanelReading):
    pass

class P1_PCC4_SolarIncomer(LTPanelReading):
    pass

class P1_PCC4_Chiller1(LTPanelReading):
    pass

class P1_PCC4_CoolingTower(LTPanelReading):
    pass

class P1_PCC4_CellLTP4(LTPanelReading):
    pass

# UPS-1 models for Phase 1
class P1_UPS1_Incomer1A(LTPanelReading):
    pass

class P1_UPS1_Incomer1B(LTPanelReading):
    pass

class P1_UPS1_Incomer1C(LTPanelReading):
    pass

class P1_UPS1_Incomer1D(LTPanelReading):
    pass

class P1_UPS1_Incomer1E(LTPanelReading):
    pass

class P1_UPS1_OG1A(LTPanelReading):
    pass

class P1_UPS1_OG1B(LTPanelReading):
    pass

class P1_UPS1_OG1C(LTPanelReading):
    pass

class P1_UPS1_OG1D(LTPanelReading):
    pass

class P1_UPS1_OG1E(LTPanelReading):
    pass

class P1_UPS1_OGSection1(LTPanelReading):
    pass

class P1_UPS1_OGSection2(LTPanelReading):
    pass

# UPS-1 LT models for Phase 1
class P1_UPS1LT1_IncomerOG3F2(LTPanelReading):
    pass

class P1_UPS1LT1_Panel1PCW(LTPanelReading):
    pass

class P1_UPS1LT2_IncomerOG4F2(LTPanelReading):
    pass

# UPS-2 models for Phase 1
class P1_UPS2_Incomer2A(LTPanelReading):
    pass

class P1_UPS2_Incomer2B(LTPanelReading):
    pass

class P1_UPS2_Incomer2C(LTPanelReading):
    pass

class P1_UPS2_Incomer2D(LTPanelReading):
    pass

class P1_UPS2_Incomer2E(LTPanelReading):
    pass

class P1_UPS2_Panel2A(LTPanelReading):
    pass

class P1_UPS2_Panel2B(LTPanelReading):
    pass

class P1_UPS2_Panel2C(LTPanelReading):
    pass

class P1_UPS2_Panel2D(LTPanelReading):
    pass

class P1_UPS2_Panel2E(LTPanelReading):
    pass

class P1_UPS2_OutgoingABC(LTPanelReading):
    pass

class P1_UPS2_LTPIncomer(LTPanelReading):
    pass

# Cell LT Panel models for Phase 1
class P1_CellLTP1_HotWaterTank1(LTPanelReading):
    pass

class P1_CellLTP1_HotWaterTank2(LTPanelReading):
    pass

class P1_CellLTP2_IncomerTF2(LTPanelReading):
    pass

class P1_CellLTP2_SINXP1(LTPanelReading):
    pass

class P1_CellLTP2_SINXP2(LTPanelReading):
    pass

class P1_CellLTP2_SINXP4(LTPanelReading):
    pass

class P1_CellLTP3_Incomer(LTPanelReading):
    pass

class P1_CellLTP3_AirCompressor1(LTPanelReading):
    pass

class P1_CellLTP3_AirCompressor2(LTPanelReading):
    pass

class P1_CellLTP3_AirCompressor3(LTPanelReading):
    pass

class P1_CellLTP3_AirCompressor4(LTPanelReading):
    pass

class P1_CellLTP4_Incomer(LTPanelReading):
    pass

class P1_CellLTP4_AHU1(LTPanelReading):
    pass

class P1_CellLTP4_AHU2(LTPanelReading):
    pass

class P1_CellLTP4_AHU3(LTPanelReading):
    pass

class P1_CellLTP4_AHU4(LTPanelReading):
    pass

class P1_CellLTP4_AHU5(LTPanelReading):
    pass

class P1_CellLTP4_Spare(LTPanelReading):
    pass

class P1_CellLTP4_AHU6(LTPanelReading):
    pass

class P1_CellLTP4_AHU7(LTPanelReading):
    pass

class P1_CellLTP4_AHU8(LTPanelReading):
    pass

class P1_CellLTP4_AHU9(LTPanelReading):
    pass

class P1_CellLTP4_AHU10(LTPanelReading):
    pass

class P1_CellLTP4_AxialFlowFan(LTPanelReading):
    pass

# Cell Tool PDB models for Phase 1
class P1_CellToolPDB1_Incomer(LTPanelReading):
    pass

class P1_CellToolPDB1_Diffusion1(LTPanelReading):
    pass

class P1_CellToolPDB1_Diffusion2(LTPanelReading):
    pass

class P1_CellToolPDB1_Diffusion3(LTPanelReading):
    pass

class P1_CellToolLTP1_Incomer(LTPanelReading):
    pass

class P1_CellToolLTP1_ALOX1(LTPanelReading):
    pass

class P1_CellToolLTP1_ALOX2(LTPanelReading):
    pass

class P1_CellToolLTP1_ALOX3(LTPanelReading):
    pass

class P1_CellToolPDB2_Incomer(LTPanelReading):
    pass

class P1_CellToolPDB2_Spare(LTPanelReading):
    pass

class P1_CellToolPDB2_SINXP3(LTPanelReading):
    pass

# Electrical Panel models for Phase 1
class P1_ElectricalPanel_Incomer(LTPanelReading):
    pass

# Inverter models for Phase 1
class P1_PepplCellLTP3(InverterReading):
    pass

class P1_PepplAHU2(InverterReading):
    pass

class P1_PepplAHU3(InverterReading):
    pass

class P1_PepplAHU4(InverterReading):
    pass

class P1_PepplAHU5(InverterReading):
    pass

class P1_PepplAHU6(InverterReading):
    pass

class P1_PepplAHU7(InverterReading):
    pass

class P1_PepplAHU10(InverterReading):
    pass

class P1_PepplAHU9(InverterReading):
    pass

class P1_PeiPelAHU5(InverterReading):
    pass

class P1_PeiPelAHU6(InverterReading):
    pass

class P1_PepplCellLTP3Repeat(InverterReading):
    pass

class P1_PeiPlAHU7(InverterReading):
    pass

class P1_PeiPlAHU8(InverterReading):
    pass
