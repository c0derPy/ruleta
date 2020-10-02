"""empty message

Revision ID: 87170b47a0f6
Revises: 
Create Date: 2020-10-02 15:15:23.600813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87170b47a0f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jugador',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=200), nullable=True),
    sa.Column('apellido', sa.String(length=200), nullable=True),
    sa.Column('dinero', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_jugador_fecha_creacion'), 'jugador', ['fecha_creacion'], unique=False)
    op.create_table('rueda',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color', sa.Enum('VERDE', 'ROJO', 'NEGRO', name='color'), nullable=True),
    sa.Column('total_apuestas', sa.Integer(), nullable=True),
    sa.Column('total_pagado', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('resultado_giro', sa.String(length=50), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rueda_fecha_creacion'), 'rueda', ['fecha_creacion'], unique=False)
    op.create_table('apuesta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dinero', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('color', sa.String(length=20), nullable=True),
    sa.Column('pago', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('jugador', sa.Integer(), nullable=False),
    sa.Column('rueda', sa.Integer(), nullable=False),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['jugador'], ['jugador.id'], ),
    sa.ForeignKeyConstraint(['rueda'], ['rueda.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apuesta_fecha_creacion'), 'apuesta', ['fecha_creacion'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_apuesta_fecha_creacion'), table_name='apuesta')
    op.drop_table('apuesta')
    op.drop_index(op.f('ix_rueda_fecha_creacion'), table_name='rueda')
    op.drop_table('rueda')
    op.drop_index(op.f('ix_jugador_fecha_creacion'), table_name='jugador')
    op.drop_table('jugador')
    # ### end Alembic commands ###
