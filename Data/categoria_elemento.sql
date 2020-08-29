USE [GFI]
GO

/****** Object:  Table [dbo].[categoria_elemento]    Script Date: 21/10/2019 9:53:49 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[categoria_elemento](
	[id_pk] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](50) NULL,
	[created_at] [datetime] NOT NULL,
	[updated_at] [datetime] NULL,
	[deleted_at] [datetime] NULL,
	[user_create] [nvarchar](50) NOT NULL,
	[user_update] [nvarchar](50) NULL,
	[user_delete] [nvarchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_pk] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO


