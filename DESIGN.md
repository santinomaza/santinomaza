# Design Document

## by Omar Alejandro Santos Jimenez

Video overview: <URL HERE>

## Scope

This database includes all the entitites necessary to facilitate the study of the life of the European honey bee **Apis mellifera**.

* __Hive__, basic information for the identification and registration of hives.
* __Bees__, basic information for the identification and registration of hives.
* __Tasks__, basic information for the identification of the tasks performed bu the bee on daily basis.
* __Enviroment__, information including flora and fauna enviromental conditions.
* __Healt__, bee heal information, deseases, treatments to maintain the bee's best living condition.

Out of the scope are elements such a type of honey, type of pollen, pollen analysis.

## Functional Requirements

* Basic operations such as CREATE, SELECT, UPDATE, DELETE.
* Tracking the enviromental conditions a bee hive endures
* Tracking common bee diseases
* Tracking the typo of activity to identify which is the most common.

`With this database it is not possible to authenticate a honey for certification.`

## Representation

Entities are captured in SQLite tables with the following schema.

### Entities

The database includes the following entities:

### Hive

`hive` table includes:

Column | Description | Type | Constrain | Key
:-:|:-:|:-:|:-:|:-:|
`id` | Unique identifier of the hive | INTEGER | NOT NULL | PRI |
`location` | Location of the hive | TEXT | NOT NULL | |
`hive_type` | Natural or artifitial | TEXT | NOT NULL CHECK | |
`hive_date_install` | Date of hive installation | NUMERIC | NOT NULL | |

All columns are required and have the `NOT NULL` constraint applied where a `PRIMARY KEY` or `FOREIGN KEY` constraint is not.

### Bees

`bees`table includes:

Column | Description | Type | Constrain | Key
:-:|:-:|:-:|:-:|:-:|
`id` | Unique identifier of the bee | INTEGER | | PRI | |
`hive_id` | Reference to the **hive** table | INTEGER | | FOREIGN |
`role` | Type of role on the hive (Queen, worker, drone) | TEXT | NOT NULL CHECK | |
`date_born`  | Date of birth | NUMERIC | NOT NULL | |
`healt_state` | Health status of the bee | TEXT | NOT NULL CHECK | |

All columns are required and have the `NOT NULL` constraint applied where a `PRIMARY KEY` or `FOREIGN KEY` constraint is not.

### Tasks

`tasks`table includes:

Column | Description | Type | Constrain | Key
:-:|:-:|:-:|:-:|:-:|
`id` | Unique identifier of the task | INTEGER | | PRI |
`bee_id` | Reference to the table **bees** | INTEGER | | FOREIGN |
`type_activity` | Type of activity performed (nectar collection, brood care, warrior)| TEXT | NOT NULL CHECK | |
`datetime_task` | Datetime of the task | NUMERIC | NOT NULL | |
`task_time` | Time lapse of the task | NUMERIC | NOT NULL | |

All columns are required and have the `NOT NULL` constraint applied where a `PRIMARY KEY` or `FOREIGN KEY` constraint is not.
The data type for `datetime task` is INTEGER, the value is minutes.

### Enviroments

`enviroments` table includes:

Column | Description | Type | Constrain | Key
:-:|:-:|:-:|:-:|:-:|
`id` | Unique identifier of the task | INTEGER | | PRI |
`hive_id` | Reference to the **hive** table | INTEGER | | FOREIGN |
`temperature` | Temperature enviroment Cº | REAL | NOT NULL
`humidity`  | Percent relative humidity | INTEGER | NOT NULL
`flora` | Description of the available flora | TEXT | NOT NULL |
`datetime_env` | Datetime of the task | NUMERIC | NOT NULL | |

All columns are required and have the `NOT NULL` constraint applied where a `PRIMARY KEY` or `FOREIGN KEY` constraint is not.
The data type for `temperature` column is `REAL` because requires negatives and decimal numbers.

### Bee Healt

`bee_healt`table includes:

Column | Description | Type | Constrain | Key
:-:|:-:|:-:|:-:|:-:|
`id` | Unique identifier of the task | INTEGER | | PRI |
`bee_id` | Reference to the table **bees** | INTEGER | | FOREIGN |
`diseases` | Diseases or conditions detected | TEXT | NOT NULL | |
`treatments`  | Treatments applied or recommended | TEXT | NOT NULL | |
`datetime_disease` | Datetime of the check or treatment | NUMERIC | NOT NULL | |

All columns are required and have the `NOT NULL` constraint applied where a `PRIMARY KEY` or `FOREIGN KEY` constraint is not.

### Relationships

The below entity relationship diagram describe the relationships among the entities in the database.

![erBeesDiagram](/workspaces/189281660/sample-project/diagram.png)

* A hive can have many bees
* The hive can coexist wih several enviroments with their different conditions.
* From the day they are born, bess have a defined role but can perform multiple activities.
* Bee healt is a condition that affects all bees in a hive.

## Optimizations

For a common or typical query for the users of this database is to know the temperatura of the enviroment almost all the time, the warming areas are the best for hives.
INDEX `temperature`, `hive_id`

Tracking the health of bees to know their current status and prevent diseases is another common query, if the bee is already sick to know what is the proper treatment.
INDEX `bee_id`, `diseases`

Location indexing improves performance when searching by location, wich helps users to locate in a timely the hive if something happend.
INDEX `location`

## Limitations

The present scheme is only designed as a tracking scheme of hive, enviroment and bee. It's considered to certify a typo of honey, the configuration of that kind of schema needs a table with poolen type, pollen analysis.
