USE [GFI]
GO

/****** Object:  Table [dbo].[clase_elemento_formulario]    Script Date: 07/11/2019 9:29:27 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[clase_elemento_formulario](
	[id_pk] [nvarchar](100) NOT NULL,
	[nombre] [nvarchar](100) NULL,
	[descripcion] [nvarchar](200) NULL,
	[codigo] [nvarchar](max) NULL,
	[categoria_elemento_id_pk] [int] NOT NULL,
	[tipo_elemento_id_pk] [int] NOT NULL,
	[institucion_id_pk] [nvarchar](100) NULL,
	[icon] [nvarchar](50) NULL,
	[permite_origen] [int] NULL,
	[created_at] [datetime] NOT NULL,
	[updated_at] [datetime] NULL,
	[deleted_at] [datetime] NULL,
	[user_create] [nvarchar](100) NOT NULL,
	[user_update] [nvarchar](100) NULL,
	[user_delete] [nvarchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_pk] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

ALTER TABLE [dbo].[clase_elemento_formulario]  WITH CHECK ADD  CONSTRAINT [Ref_clase_agrupador_formulario_to_categoria_elemento] FOREIGN KEY([categoria_elemento_id_pk])
REFERENCES [dbo].[categoria_elemento] ([id_pk])
GO

ALTER TABLE [dbo].[clase_elemento_formulario] CHECK CONSTRAINT [Ref_clase_agrupador_formulario_to_categoria_elemento]
GO

ALTER TABLE [dbo].[clase_elemento_formulario]  WITH CHECK ADD  CONSTRAINT [Ref_clase_elemento_formulario_to_institucion] FOREIGN KEY([institucion_id_pk])
REFERENCES [dbo].[institucion] ([id_pk])
GO

ALTER TABLE [dbo].[clase_elemento_formulario] CHECK CONSTRAINT [Ref_clase_elemento_formulario_to_institucion]
GO

ALTER TABLE [dbo].[clase_elemento_formulario]  WITH CHECK ADD  CONSTRAINT [Ref_clase_elemento_formulario_to_tipo_elemento] FOREIGN KEY([tipo_elemento_id_pk])
REFERENCES [dbo].[tipo_elemento] ([id_pk])
GO

ALTER TABLE [dbo].[clase_elemento_formulario] CHECK CONSTRAINT [Ref_clase_elemento_formulario_to_tipo_elemento]
GO


