MODULE {{data.name}} IMPLEMENTED_BY  {{data.name}} 
SEC std.MetaData
    Desc       := TL_{{data.name}}.Desc ;
    Category   := {{data.category}} ;
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
