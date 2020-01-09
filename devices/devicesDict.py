#Note: Profile Monitor and shutter dict = 'device_name': (moverCommand,moverRB,insertVal,retractVal, insertRB, retractRB)
pmDict = {'YAG01' : ('YAGS:IN20:211:PNEUMATIC','YAGS:IN20:211:TGT_STS',1,0,2,1),
          'YAGG1' : ('YAGS:IN20:841:PNEUMATIC','YAGS:IN20:841:TGT_STS',1,0,2,1),
          'YAG02' : ('YAGS:IN20:241:PNEUMATIC','YAGS:IN20:241:TGT_STS',1,0,2,1),
          'YAG03' : ('YAGS:IN20:351:PNEUMATIC','YAGS:IN20:351:TGT_STS',1,0,2,1),
          'YAGS1' : ('YAGS:IN20:921:PNEUMATIC','YAGS:IN20:921:TGT_STS',0,1,1,2),#FLAG
          'YAGS2' : ('YAGS:IN20:995:PNEUMATIC','YAGS:IN20:995:TGT_STS',1,0,2,1),
          'YAG01B': ('YAGS:GUNB:753:PNEUMATIC','YAGS:GUNB:753:TGT_STS',1,0,2,1),
          'OTRH1' : ('OTRS:IN20:465:PNEUMATIC','OTRS:IN20:465:TGT_STS',1,0,2,1),
          'OTRH2' : ('OTRS:IN20:471:PNEUMATIC','OTRS:IN20:471:TGT_STS',1,0,2,1),
          'OTR01' : ('OTRS:IN20:541:PNEUMATIC','OTRS:IN20:541:TGT_STS',1,0,2,1),
          'OTR02' : ('OTRS:IN20:571:PNEUMATIC','OTRS:IN20:571:TGT_STS',1,0,2,1),
          'OTR03' : ('OTRS:IN20:621:PNEUMATIC','OTRS:IN20:621:TGT_STS',0,1,1,2),#FLAG
          'OTR04' : ('OTRS:IN20:711:PNEUMATIC','OTRS:IN20:711:TGT_STS',0,1,1,2),#FLAG
          'OTR11' : ('OTRS:LI21:237:PNEUMATIC','OTRS:LI21:237:TGT_STS',0,1,1,2),#FLAG
          'OTR12' : ('OTRS:LI21:291:PNEUMATIC','OTRS:LI21:291:TGT_STS',0,1,1,2),#FLAG
          'OTR21' : ('OTRS:LI24:807:PNEUMATIC','OTRS:LI24:807:TGT_STS',1,0,2,1)}

shutterDict = {'GunRF' : ('IOC:BSY0:MP01:PCELLCTL','IOC:BSY0:MP01:PCELLCTL',0,1,0,1),
               'MechShutLCLS1' : ('IOC:BSY0:MP01:MSHUTCTL','IOC:BSY0:MP01:MSHUTCTL',0,1,0,1),
               'LHShutter' : ('IOC:BSY0:MP01:MSHUTCTL','IOC:BSY0:MP01:MSHUTCTL',0,1,0,1),
               'TD11' : ('DUMP:LI21:305:TD11_PNEU','DUMP:LI21:305:TGT_STS',0,1,2,1),
               'BYKIK': ('IOC:BSY0:MP01:BYKIKCTL','IOC:BSY0:MP01:BYKIKCTL',0,1,0,1),
               'MechShutLCLS2' : ('SIOC:SYS2:MP01:DISABLE_BEAM','SHUT:GUNB:100:CLOSED_STATUS_MPSC',1,0,1,0),
               'AOM' : ('SIOC:SYS2:MP01:DISABLE_AOM','SIOC:SYS2:MP01:DISABLE_AOM',1,0,1,0)}

#Note: RF dict = 'device_name' : (gunPhaseSetting, gunPhaseReadBack, gunAmplitudeSetting, gunAmplitudeReadBack)
rfDict = {'LCLS1L1S' : ('ACCL:LI21:1:L1S_PDES','ACCL:LI21:1:L1S_S_PV','ACCL:LI21:1:L1S_ADES','ACCL:LI21:1:L1S_S_AV'),
          'LCLS1L1X' : ('ACCL:LI21:180:L1X_PDES','ACCL:LI21:180:L1X_S_PV','ACCL:LI21:180:L1X_ADES','ACCL:LI21:180:L1X_S_AV'),
          'LCLS1LOA' : ('ACCL:IN20:300:L0A_PDES','ACCL:IN20:300:L0A_S_PV','ACCL:IN20:300:L0A_ADES','ACCL:IN20:300:L0A_S_AV'),
          'LCLS1LOB' : ('ACCL:IN20:400:L0B_PDES','ACCL:IN20:400:L0B_S_PV','ACCL:IN20:400:L0B_ADES','ACCL:IN20:400:L0B_S_AV'),
          'LCLS1GUN' : ('GUN:IN20:1:GN1_PDES','GUN:IN20:1:GN1_S_PV','GUN:IN20:1:GN1_ADES','GUN:IN20:1:GN1_S_AV'),
          'LCLS2GUN' : ('GUN:GUNB:100:POPEN','GUN:GUNB:100:PACT','GUN:GUNB:100:AOPEN','GUN:GUNB:100:AACT'),
          #Note: 'device_name' : (PhaseSetting,PhaseReadBack,AmplitudeSetting,AmplitudeReadBack,OffsetSetting)
          'Buncher'  : ('ACCL:GUNB:455:POPEN','ACCL:GUNB:455:PACT','ACCL:GUNB:455:AOPEN','ACCL:GUNB:455:AACT','ACCL:GUNB:455:CAV1:GOLD')}

#Note: BPM dict = 'device_name' : (xreadback,yreadback,tmitreadback)
bpmDict = {'BPM1B' : ('BPMS:GUNB:314:X','BPMS:GUNB:314:Y','BPMS:GUNB:314:TMIT'),
           'BPM2B' : ('BPMS:GUNB:925:X','BPMS:GUNB:925:Y','BPMS:GUNB:925:TMIT')}

#Note: laser dict = 'device_name' : (LaserPhaseSetting,LaserPhaseOffset,rfFeedback,shutterRB) [Need LCLS2 Laser PV Name]
laserDict = {'Vitara1' : ('OSC:LR20:20:PDES','OSC:LR20:20:POC','ALRM:SYS0:VITARA1:ALHBERR','SHTR:LR20:100:UV_STS'),
             'Vitara2' : ('OSC:LR20:10:PDES','OSC:LR20:10:POC','ALRM:SYS0:VITARA2:ALHBERR','SHTR:LR20:90:UV_STS')}

#Note: mirror dict = 'device_name' : (mirrorSettingH,mirrorReadbackH,mirrorSettingV,mirrorReadbackV)
mirrorDict = {'LCLS1M13' : ('MIRR:LR20:125:M13_MOTR_H','MIRR:LR20:125:M13_MOTR_V',),
              'LCLS1M12' : ('MIRR:LR20:150:M12_MOTR_H','MIRR:LR20:150:M12_MOTR_V'),
              'LCLS1M6'  : ('MIRR:LR20:121:M6_MOTR_H','MIRR:LR20:121:M6_MOTR_V'),
              'LCLS1M5'  : ('MIRR:IN20:122:M5_MOTR_H','MIRR:IN20:122:M5_MOTR_V'),
              'LCLS1M3'  : ('MIRR:IN20:161:M3_MOTR_H','MIRR:IN20:161:M3_MOTR_V'),
              'LCLS1M2'  : ('MIRR:IN20:162:M2_MOTR_H','MIRR:IN20:162:M2_MOTR_V'),
              'LCLS2M12' : ('MIRR:LGUN:510:M12_MOTR_H','MIRR:LGUN:510:M12_MOTR_V'),
              'LCLS2M6'  : ('MIRR:LGUN:700:M6_MOTR_H','MIRR:LGUN:700:M6_MOTR_V'),
              'LCLS2M4'  : ('MIRR:LGUN:800:M4_MOTR_H','MIRR:LGUN:800:M4_MOTR_V'),
              'LCLS2M3'  : ('MIRR:LGUN:820:M3_MOTR_H','MIRR:LGUN:820:M3_MOTR_V')}



