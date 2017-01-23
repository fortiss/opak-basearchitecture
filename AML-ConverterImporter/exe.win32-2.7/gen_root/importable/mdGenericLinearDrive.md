MODULE GenericLinearDrive IMPLEMENTED_BY  GenericLinearDrive 
SEC std.MetaData
    Desc       := TL_GenericLinearDrive.Desc ;
    Category   := 'Component'|'KinematicElements'|'ActiveLinearElement' ;
    Icon_16    := IP_GenericLinearDrive.Icon_16 ;
    Icon_32    := IP_GenericLinearDrive.Icon_32 ;
END_SEC

SEC std.Parameters

	SEC Param : eTechnology
		Variable := eTechnology;
		Name := TL_GenericLinearDrive.Name_eTechnology;
		Desc := TL_GenericLinearDrive.Desc_eTechnology;
	END_SEC

END_SEC
