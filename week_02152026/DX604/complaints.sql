-- =============================================
-- NHTSA Complaints Table Creation Script
-- =============================================
-- Description: Creates the complaints table for NHTSA vehicle complaint data
-- Uses NVARCHAR for text columns to handle Unicode characters
-- Column lengths are based on the reference specification
-- =============================================

CREATE TABLE kgcomplaints (
    -- Primary identifier
    CMPLID NVARCHAR(9) NOT NULL,
    
    -- Reference and identification fields
    ODINO NVARCHAR(9),
    MFR_NAME NVARCHAR(40),
    MAKETXT NVARCHAR(25),
    MODELTXT NVARCHAR(256),
    YEARTXT NVARCHAR(4),
    
    -- Incident indicators
    CRASH NVARCHAR(1),
    FAILDATE NVARCHAR(8),
    FIRE NVARCHAR(1),
    INJURED NUMERIC(2),
    DEATHS NUMERIC(2),
    
    -- Component and location information
    COMPDESC NVARCHAR(128),
    CITY NVARCHAR(30),
    STATE NVARCHAR(2),
    VIN NVARCHAR(11),
    
    -- Date fields
    DATEA NVARCHAR(8),
    LDATE NVARCHAR(8),
    
    -- Vehicle metrics
    MILES NUMERIC(7),
    OCCURENCES NUMERIC(4),
    
    -- Complaint details
    CDESCR NVARCHAR(2048),
    CMPL_TYPE NVARCHAR(4),
    
    -- Additional incident information
    POLICE_RPT_YN NVARCHAR(1),
    PURCH_DT NVARCHAR(8),
    ORIG_OWNER_YN NVARCHAR(1),
    
    -- Vehicle features
    ANTI_BRAKES_YN NVARCHAR(1),
    CRUISE_CONT_YN NVARCHAR(1),
    NUM_CYLS NUMERIC(2),
    DRIVE_TRAIN NVARCHAR(4),
    
    -- Fuel system information
    FUEL_SYS NVARCHAR(4),
    FUEL_TYPE NVARCHAR(4),
    
    -- Transmission and speed
    TRANS_TYPE NVARCHAR(4),
    VEH_SPEED NUMERIC(3),
    
    -- Tire information
    DOT NVARCHAR(20),
    TIRE_SIZE NVARCHAR(30),
    LOC_OF_TIRE NVARCHAR(4),
    TIRE_FAIL_TYPE NVARCHAR(4),
    ORIG_EQUIP_YN NVARCHAR(1),
    MANUF_DT NVARCHAR(8),
    
    -- Child restraint information
    SEAT_TYPE NVARCHAR(4),
    RESTRAINT_TYPE NVARCHAR(4),
    
    -- Dealer information
    DEALER_NAME NVARCHAR(40),
    DEALER_TEL NVARCHAR(20),
    DEALER_CITY NVARCHAR(30),
    DEALER_STATE NVARCHAR(2),
    DEALER_ZIP NVARCHAR(10),
    
    -- Product classification
    PROD_TYPE NVARCHAR(4),
    
    -- Resolution indicators
    REPAIRED_YN NVARCHAR(1),
    MEDICAL_ATTN NVARCHAR(1),
    VEHICLES_TOWED_YN NVARCHAR(1),
    
    -- Primary key constraint
    CONSTRAINT PK_kgcomplaints PRIMARY KEY (CMPLID)
);

-- =============================================
-- Create indexes for common query patterns
-- =============================================

-- Index on manufacturer and make for filtering
CREATE INDEX IX_complaints_MFR_MAKE ON kgcomplaints (MFR_NAME, MAKETXT);

-- Index on model year for time-series analysis
CREATE INDEX IX_complaints_YEAR ON kgcomplaints (YEARTXT);

-- Index on date added to file (for homework queries)
CREATE INDEX IX_complaints_DATEA ON kgcomplaints (DATEA);

-- Index on date complaint received
CREATE INDEX IX_complaints_LDATE ON kgcomplaints (LDATE);

-- Index on state for geographic analysis
CREATE INDEX IX_complaints_STATE ON kgcomplaints (STATE);

-- Index on complaint type for categorization
CREATE INDEX IX_complaints_CMPL_TYPE ON kgcomplaints (CMPL_TYPE);

-- Index on product type for filtering
CREATE INDEX IX_complaints_PROD_TYPE ON kgcomplaints (PROD_TYPE);


-- =============================================
-- Add comments/extended properties (SQL Server)
-- =============================================

EXEC sp_addextendedproperty 
    @name = N'MS_Description', 
    @value = N'NHTSA internal unique sequence number. Updateable field.', 
    @level0type = N'SCHEMA', @level0name = N'dbo',
    @level1type = N'TABLE',  @level1name = N'kgcomplaints',
    @level2type = N'COLUMN', @level2name = N'CMPLID';

EXEC sp_addextendedproperty 
    @name = N'MS_Description', 
    @value = N'NHTSA internal reference number. May be repeated for multiple components.', 
    @level0type = N'SCHEMA', @level0name = N'dbo',
    @level1type = N'TABLE',  @level1name = N'kgcomplaints',
    @level2type = N'COLUMN', @level2name = N'ODINO';

EXEC sp_addextendedproperty 
    @name = N'MS_Description', 
    @value = N'Description of the complaint (max 2048 characters)', 
    @level0type = N'SCHEMA', @level0name = N'dbo',
    @level1type = N'TABLE',  @level1name = N'kgcomplaints',
    @level2type = N'COLUMN', @level2name = N'CDESCR';

-- =============================================
-- Script Complete
-- =============================================
