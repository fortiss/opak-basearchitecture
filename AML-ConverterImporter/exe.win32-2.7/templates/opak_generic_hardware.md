MODULE {{data.name}} IMPLEMENTED_BY  {{data.name}} 
SEC std.MetaData
    Desc       := TL_{{data.name}}.Desc ;
    Category   := {{data.get_category_string()}} ;
    Icon_16    := IP_{{data.name}}.Icon_16 ;
    Icon_32    := IP_{{data.name}}.Icon_32 ;
END_SEC
{% if (data.params|length)!=0 %}
SEC std.Parameters
{% for p in data.params %}
	SEC Param : {{p.name}}
		Variable := {{p.name}};
		Name := TL_{{data.name}}.Name_{{p.name}};
		Desc := TL_{{data.name}}.Desc_{{p.name}};
	END_SEC
{% endfor %}
END_SEC
{% endif %}
{% if data.collada_uri is string %}
SEC CAD
  SEC Pose: BaseElement
    Variable := {{data.name}}
    File := "CAD/{{data.name}}.dae"
    SEC Translation
      RX := 0;
      RY := 0;
      RZ := 0;
      SX := 0.01;
      SY := 0.01;
      SZ := 0.01;
      TX := 2;
      TY := 2;
      TZ := 2;
     END_SEC  
END_SEC
{% endif %}