# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-06-14 06:49:32
"""
import arcpy
from arcpy.ia import *
from arcpy.ia import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *

def Model():  # Model

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("ImageAnalyst")
    arcpy.CheckOutExtension("ImageExt")

    drogi = "PL.PZGiK.330.1463__OT_SKDR_L"
    przystanki = "PL.PZGiK.330.1463__OT_OIKM_P"
    tereny_zielone = "PL.PZGiK.330.1463__OT_PTLZ_A"
    zabudowa = "PL.PZGiK.330.1463__OT_PTZB_A"
    Radom_NMPT_tif = arcpy.Raster("Radom_NMPT.tif")
    Radom_NMPT_tif_2_ = arcpy.Raster("Radom_NMPT.tif")
    Input_true_raster_or_constant_value = 1
    Input_false_raster_or_constant_value_3_ = 0
    radom = "radom"

    # Process: Polyline to Raster (Polyline to Raster) (conversion)
    drogi_raster = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\drogi_raster"
    arcpy.conversion.PolylineToRaster(in_features=drogi, value_field="length", out_rasterdataset=drogi_raster)

    # Process: Euclidean Distance (Euclidean Distance) (sa)
    drogi_odl = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\drogi_odl"
    Euclidean_Distance = drogi_odl
    Output_direction_raster = ""
    Out_back_direction_raster = ""
    drogi_odl = arcpy.sa.EucDistance(drogi_raster, None, "56", Output_direction_raster, "PLANAR", "", Out_back_direction_raster)
    drogi_odl.save(Euclidean_Distance)


    # Process: Point to Raster (Point to Raster) (conversion)
    przystanki_raster = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\przystanki_raster"
    arcpy.conversion.PointToRaster(in_features=przystanki, value_field="FID", out_rasterdataset=przystanki_raster)

    # Process: Euclidean Distance (2) (Euclidean Distance) (sa)
    przystanki_odl = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\przystanki_odl"
    Euclidean_Distance_2_ = przystanki_odl
    Output_direction_raster_2_ = ""
    Out_back_direction_raster_2_ = ""
    przystanki_odl = arcpy.sa.EucDistance(przystanki_raster, None, "47", Output_direction_raster_2_, "PLANAR", "", Out_back_direction_raster_2_)
    przystanki_odl.save(Euclidean_Distance_2_)


    # Process: Polygon to Raster (Polygon to Raster) (conversion)
    tereny_zielone_raster = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\tereny_zielone_raster"
    arcpy.conversion.PolygonToRaster(in_features=tereny_zielone, value_field="area", out_rasterdataset=tereny_zielone_raster)

    # Process: Euclidean Distance (3) (Euclidean Distance) (sa)
    tereny_zielone_odl = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\tereny_zielone_odl"
    Euclidean_Distance_3_ = tereny_zielone_odl
    Output_direction_raster_3_ = ""
    Out_back_direction_raster_3_ = ""
    tereny_zielone_odl = arcpy.sa.EucDistance(tereny_zielone_raster, None, "56", Output_direction_raster_3_, "PLANAR", "", Out_back_direction_raster_3_)
    tereny_zielone_odl.save(Euclidean_Distance_3_)


    # Process: Polygon to Raster (2) (Polygon to Raster) (conversion)
    zabudowa_raster = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\zabudowa_raster"
    arcpy.conversion.PolygonToRaster(in_features=zabudowa, value_field="area", out_rasterdataset=zabudowa_raster)

    # Process: Euclidean Distance (4) (Euclidean Distance) (sa)
    zabudowa_odl = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\zabudowa_odl"
    Euclidean_Distance_4_ = zabudowa_odl
    Output_direction_raster_4_ = ""
    Out_back_direction_raster_4_ = ""
    zabudowa_odl = arcpy.sa.EucDistance(zabudowa_raster, None, "56", Output_direction_raster_4_, "PLANAR", "", Out_back_direction_raster_4_)
    zabudowa_odl.save(Euclidean_Distance_4_)


    # Process: Reclassify (Reclassify) (sa)
    drogi_reclass = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\drogi_reclass"
    Reclassify = drogi_reclass
    drogi_reclass = arcpy.sa.Reclassify(drogi_odl, "VALUE", "0 233,922760 10;233,922760 637,971163 9;637,971163 1105,816682 8;1105,816682 1594,927907 7;1594,927907 2084,039131 6;2084,039131 2594,416062 5;2594,416062 3126,058697 4;3126,058697 3700,232744 3;3700,232744 4359,469612 2;4359,469612 5422,754883 1", "DATA")
    drogi_reclass.save(Reclassify)


    # Process: Reclassify (4) (Reclassify) (sa)
    przystanki_reclass = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\przystanki_reclass"
    Reclassify_4_ = przystanki_reclass
    przystanki_reclass = arcpy.sa.Reclassify(przystanki_odl, "VALUE", "0 272,497223 10;272,497223 583,922622 9;583,922622 934,276195 8;934,276195 1323,557943 7;1323,557943 1771,231953 6;1771,231953 2296,762312 5;2296,762312 2861,220847 4;2861,220847 3425,679381 3;3425,679381 4009,602003 2;4009,602003 4963,342285 1", "DATA")
    przystanki_reclass.save(Reclassify_4_)


    # Process: Reclassify (3) (Reclassify) (sa)
    tereny_zielone_reclass = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\tereny_zielone_reclass"
    Reclassify_3_ = tereny_zielone_reclass
    tereny_zielone_reclass = arcpy.sa.Reclassify(tereny_zielone_odl, "VALUE", "0 233,250000 10;233,250000 629,775000 9;629,775000 1119,600000 8;1119,600000 1632,750000 7;1632,750000 2169,225000 6;2169,225000 2729,025000 5;2729,025000 3312,150000 4;3312,150000 3918,600000 3;3918,600000 4665 2;4665 5947,875000 1", "DATA")
    tereny_zielone_reclass.save(Reclassify_3_)


    # Process: Reclassify (2) (Reclassify) (sa)
    zabudowa_reclass = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\zabudowa_reclass"
    Reclassify_2_ = zabudowa_reclass
    zabudowa_reclass = arcpy.sa.Reclassify(zabudowa_odl, "VALUE", "0 239,871678 1;239,871678 654,195485 2;654,195485 1133,938840 3;1133,938840 1635,488712 4;1635,488712 2158,845100 5;2158,845100 2682,201488 6;2682,201488 3227,364392 7;3227,364392 3794,333812 8;3794,333812 4448,529297 9;4448,529297 5560,661621 10", "DATA")
    zabudowa_reclass.save(Reclassify_2_)


    # Process: Surface Parameters (Surface Parameters) (sa)
    slope = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\slope"
    Surface_Parameters = slope
    slope = arcpy.sa.SurfaceParameters(Radom_NMPT_tif, "SLOPE", "QUADRATIC", "0.5 Meters", "FIXED_NEIGHBORHOOD", "METER", "DEGREE", "GEODESIC_AZIMUTHS", "NORTH_POLE_ASPECT", Radom_NMPT_tif_2_)
    slope.save(Surface_Parameters)


    # Process: Con (2) (Con) (sa)
    slope_con = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\slope_con"
    Con_2_ = slope_con
    slope_con = arcpy.sa.Con(slope, slope, "", "VALUE < 15")
    slope_con.save(Con_2_)


    # Process: Raster Calculator (Raster Calculator) (sa)
    wynik = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\myproject\\myproject.gdb\\wynik"
    Raster_Calculator = wynik
    wynik =  0.6*drogi_reclass+0.7*przystanki_reclass +0.6*tereny_zielone_reclass+ 2.5*zabudowa_reclass+ 1.3*slope_con
    wynik.save(Raster_Calculator)


    # Process: Reclassify (5) (Reclassify) (sa)
    reklasyfikacja_wyniku = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\reklasyfikacja_wyniku"
    Reclassify_5_ = reklasyfikacja_wyniku
    reklasyfikacja_wyniku = arcpy.sa.Reclassify(wynik, "VALUE", "3,600000 4,398823 1;4,398823 5,083529 2;5,083529 5,768235 3;5,768235 6,567059 4;6,567059 7,365882 5;7,365882 8,164706 6;8,164706 8,963529 7;8,963529 9,762353 8;9,762353 10,675294 9;10,675294 11,360000 10;11,360000 12,044706 11;12,044706 12,843530 12;12,843530 13,756471 13;13,756471 14,555294 14;14,555294 15,240000 15;15,240000 16,038824 16;16,038824 16,723530 17;16,723530 17,636471 18;17,636471 18,321177 19;18,321177 19,005883 20;19,005883 19,918824 21;19,918824 20,717647 22;20,717647 21,402353 23;21,402353 22,315295 24;22,315295 23 25;23 23,798824 26;23,798824 24,825883 27;24,825883 25,624706 28;25,624706 26,537648 29;26,537648 28,135295 30;28,135295 30,417648 31;30,417648 32,700001 32;NODATA 0", "DATA")
    reklasyfikacja_wyniku.save(Reclassify_5_)


    # Process: Region Group (Region Group) (sa)
    Regiony = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\Regiony"
    Region_Group = Regiony
    Regiony = arcpy.sa.RegionGroup(reklasyfikacja_wyniku, "FOUR", "WITHIN", "ADD_LINK", None)
    Regiony.save(Region_Group)


    # Process: Zonal Statistics as Table (Zonal Statistics as Table) (ia)
    ZonalTable2 = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\ZonalTable2"
    arcpy.ia.ZonalStatisticsAsTable(Regiony, "VALUE", Regiony, ZonalTable2, "DATA", "ALL", "CURRENT_SLICE", [90], "AUTO_DETECT", "ARITHMETIC", 360)
    .save(Zonal_Statistics_as_Table)


    # Process: Join Field (Join Field) (management)
    Zonal_2_ = arcpy.management.JoinField(in_data=Regiony, in_field="OBJECTID", join_table=ZonalTable2, join_field="OBJECTID")[0]

    # Process: Con (Con) (sa)
    Wynik_z_powierzchnia = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\Wynik_z_powierzchnia"
    Con = Wynik_z_powierzchnia
    Wynik_z_powierzchnia = arcpy.sa.Con(Zonal_2_, Input_true_raster_or_constant_value, Input_false_raster_or_constant_value_3_, "AREA > 400000")
    Wynik_z_powierzchnia.save(Con)


    # Process: Set Null (Set Null) (ia)
    SetNull_wyni2 = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\SetNull_wyni2"
    Set_Null = SetNull_wyni2
    SetNull_wyni2 = arcpy.ia.SetNull(Wynik_z_powierzchnia, Wynik_z_powierzchnia, "Value = 0")
    SetNull_wyni2.save(Set_Null)


    # Process: Extract by Mask (Extract by Mask) (sa)
    ostateczny_wynik = "E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb\\ostateczny_wynik"
    Extract_by_Mask = ostateczny_wynik
    ostateczny_wynik = arcpy.sa.ExtractByMask(SetNull_wyni2, radom, "INSIDE", "643346.72 389428.59 655050.72 402420.59 PROJCS[\"ETRS_1989_Poland_CS92\".GEOGCS[\"GCS_ETRS_1989\".DATUM[\"D_ETRS_1989\".SPHEROID[\"GRS_1980\".6378137.0.298.257222101]].PRIMEM[\"Greenwich\".0.0].UNIT[\"Degree\".0.0174532925199433]].PROJECTION[\"Transverse_Mercator\"].PARAMETER[\"False_Easting\".500000.0].PARAMETER[\"False_Northing\".-5300000.0].PARAMETER[\"Central_Meridian\".19.0].PARAMETER[\"Scale_Factor\".0.9993].PARAMETER[\"Latitude_Of_Origin\".0.0].UNIT[\"Meter\".1.0]]")
    ostateczny_wynik.save(Extract_by_Mask)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb", workspace="E:\\GEOINFORMACJA\\VI semestr\\decyzje\\dane\\projekt\\MyProject\\MyProject.gdb"):
        Model()
