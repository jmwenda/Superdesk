'''
Created on Aug 23, 2011

@package: superdesk person
@copyright: 2012 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Mihai Balaceanu

Contains the SQL alchemy meta for person API.
'''

from ..api.person import Person
from sqlalchemy.dialects.mysql.base import INTEGER
from sqlalchemy.schema import Column
from sqlalchemy.types import String
from superdesk.meta.metadata_superdesk import Base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.expression import case

# --------------------------------------------------------------------

class PersonMapped(Base, Person):
    '''
    Provides the mapping for Person entity.
    '''
    __tablename__ = 'person'
    __table_args__ = dict(mysql_engine='InnoDB', mysql_charset='utf8')

    Id = Column('id', INTEGER(unsigned=True), primary_key=True)
    FirstName = Column('first_name', String(255))
    LastName = Column('last_name', String(255))
    Address = Column('address', String(255))
    @hybrid_property
    def Name(self):
        if self.FirstName is not None: return self.FirstName + ' ' + self.LastName
        else: return self.FirstName

    # Expression for hybrid ------------------------------------
    @classmethod
    @Name.expression
    def _Name(cls):
        return case([(cls.FirstName != None, cls.FirstName + ' ' + cls.LastName)], else_=cls.LastName)


#TODO: add validation
#validateManaged(PersonMapped.Name)
#registerValidation(PersonMapped)
