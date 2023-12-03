from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "is_delete" BOOL   DEFAULT False,
    "created" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "modified" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "account" VARCHAR(50)  UNIQUE,
    "username" VARCHAR(50),
    "password" VARCHAR(100) NOT NULL,
    "phone" VARCHAR(15),
    "email" VARCHAR(30),
    "signature" VARCHAR(100),
    "avatar" VARCHAR(100),
    "sex" VARCHAR(20) NOT NULL  DEFAULT '保密',
    "group_id" INT REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_users_account_6c092b" ON "users" ("account");
CREATE INDEX IF NOT EXISTS "idx_users_phone_f72cc5" ON "users" ("phone");
CREATE INDEX IF NOT EXISTS "idx_users_email_133a6f" ON "users" ("email");
COMMENT ON COLUMN "users"."is_delete" IS '是否删除';
COMMENT ON COLUMN "users"."created" IS '创建时间';
COMMENT ON COLUMN "users"."modified" IS '最后修改时间';
COMMENT ON COLUMN "users"."account" IS '账号';
COMMENT ON COLUMN "users"."username" IS '用户名_昵称';
COMMENT ON COLUMN "users"."password" IS '密码';
COMMENT ON COLUMN "users"."phone" IS '手机号';
COMMENT ON COLUMN "users"."email" IS '邮箱';
COMMENT ON COLUMN "users"."signature" IS '签名';
COMMENT ON COLUMN "users"."avatar" IS '头像地址';
COMMENT ON COLUMN "users"."sex" IS '性别';
CREATE TABLE IF NOT EXISTS "token" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "token" VARCHAR(255),
    "user_id" INT REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "usergroup" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "is_delete" BOOL   DEFAULT False,
    "created" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "modified" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(50) NOT NULL
);
COMMENT ON COLUMN "usergroup"."is_delete" IS '是否删除';
COMMENT ON COLUMN "usergroup"."created" IS '创建时间';
COMMENT ON COLUMN "usergroup"."modified" IS '最后修改时间';
COMMENT ON COLUMN "usergroup"."name" IS '用户组名称';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
