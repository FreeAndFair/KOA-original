package ie.koa;

/**
 * The Ballot class represents a ballot paper in an Irish election,
 * which uses the Proportional Representation Single Transferable Vote
 * (PRSTV) system.
 * 
 * @author Dermot Cochran
 * @copyright Systems Research Group and University College Dublin, Ireland.
 * @reviewer Joe Kiniry
 * 
 * @see <a href="http://www.cev.ie/htm/tenders/pdf/1_2.pdf">Department of 
 * Environment and Local Government, Count Requirements and Commentary on Count 
 * Rules, sections 3-14</a>
 */

public class Ballot {
	
  /** 
   * Candidate ID value to use for nontransferable ballot papers.
   * 
   * @design A special candidate ID value is used to indicate
   *   non-transferable votes i.e., when the list of preferences has
   *   been exhausted and none of the continuing candidates are in the
   *   preference list, then the ballot is deemed to be nontransferable.
   *   
   * @see <a href="http://www.cev.ie/htm/tenders/pdf/1_2.pdf">Department of 
   * Environment and Local Government, Count Requirements and Commentary on Count 
   * Rules, section 7, pages 23-27</a> 
   */
  public static final long NONTRANSFERABLE;
  
  /** @review kiniry 8 Feb 2006 - Each of these fields needs at least
   * one invariant, typically.  E.g., can ballotID be negative?  If
   * ballotID is unique per Ballot object, then this needs to be
   * expressed in an invariant.  These examples are below. */

  /** Ballot ID number */
  //@ public invariant 0 < ballotID;
  /*@ public instance invariant (\forall Ballot a,b; 
    @                            a != null && b != null;
    @                            a.ballotID == b.ballotID <==> a == b);
    @*/
  protected /*@ spec_public @*/ long ballotID;
  
  /** Candidate ID to which this ballot is assigned */
  //@ public invariant (0 < candidateID) || (candidateID == NONTRANSFERABLE);
  /*@ public invariant (0 <= positionInList && 
    @                  positionInList < numberOfPreferences) ==>
    @                  candidateID == preferenceList[positionInList];
    @ public invariant (positionInList == numberOfPreferences) ==>
    @                  candidateID == NONTRANSFERABLE;
    @*/
  protected /*@ spec_public @*/ long candidateID;

  /** Preference list of candidate IDs */
  /*@ public invariant (\forall int i; 
    @                  0 <= i && i < numberOfPreferences;
    @                  preferenceList[i] > 0 &&
    @                  preferenceList[i] != NONTRANSFERABLE);
    @ public invariant (\forall int i, j; 
    @                  0 < i && i < numberOfPreferences && 0 <= j && j < i;
    @                  preferenceList[i] != preferenceList[j]);
    @*/
  protected /*@ spec_public non_null @*/ long[] preferenceList;
  
  /** Total number of valid preferences on the ballot paper */
  //@ public invariant 0 < numberOfPreferences;
  protected /*@ spec_public @*/ long numberOfPreferences;
  
  /** Position within preference list */
  //@ public initially positionInList == 0;
  //@ public invariant 0 <= positionInList;
  //@ public invariant positionInList <= numberOfPreferences;
  //@ public constraint \old(positionInList) <= positionInList;
  protected /*@ spec_public @*/ int positionInList;
 

  /** @review kiniry 8 Feb 2006 - I presume that these arrays should
   * be non_null.  Note that in the latest JML tools release, and in
   * the upcoming ESC/Java2 release, non_null is the default semantics
   * of references. */
  /** Candidate ID to which the vote is assigned at the end of each count */
  protected /*@ spec_public non_null @*/ long[] candidateIDAtCount;
  
  /** Last count number in which this ballot was transfered */
  //@ public invariant 0 <= countNumberAtLastTransfer;
  //@ public initially countNumberAtLastTransfer == 0;
  protected /*@ spec_public @*/ long countNumberAtLastTransfer;
  
  /** Random number used for propotional distribution of surplus votes */
  /*@ public invariant (\forall Ballot a, b; a != null && b != null;
    @   (a.randomNumber == b.randomNumber) <==> (a == b));
    @ public constraint randomNumber == \old (randomNumber);
    @*/
  protected /*@ spec_public @*/ long randomNumber;
  
  /**
   * Default constructor
   */
  /*@ public normal_behavior
    @   ensures numberOfPreferences == 0;
    @   ensures countNumberAtLastTransfer == 0;
    @   ensures positionInList == 0;
    @   ensures candidateID == NONTRANSFERABLE;
    @   ensures ballotID > 0;
    @*/
  public /*@ pure @*/ Ballot();
  
  /**
   * Copy constructor
   * 
   * @return An exact copy of this ballot paper 
   */
  /*@ public normal_behavior
    @   ensures this == \result;
    @*/
  public /*@ pure @*/ Ballot copy();
  
  /**
   * Get the location of the ballot at each count
   * 
   * @param countNumber
   * @return The candidate ID or the NONTRANSFERABLE constant
   * @review kiniry 8 Feb 2006 - Note the rewrite of precondition to
   * make range more obvious.  I have rewritten several other
   * specifications in a similar fashion, but only in this class.
   */
  /*@ public normal_behavior
    @   requires 0 <= countNumber;
    @   requires countNumber <= countNumberAtLastTransfer;
    @   ensures \result == candidateIDAtCount[countNumber];
    @*/
  public /*@ pure @*/ long getPreferenceAtCount(int countNumber);
  
  /**
   * Get the count number for the last transfer of this ballot
   * @return The last count at which this ballot was transfered
   */
  /*@ public normal_behavior
    @   ensures \result == countNumberAtLastTransfer;
    @*/
  public /*@ pure @*/ long getCountNumberAtLastTransfer();
  
  /**
   * Get first preference vote from this ballot
   * 
   * @design There must always be a first preference vote in each
   *   ballot, otherwise the vote is not included and need not be
   *   loaded.  The quota is calculated from the number of first
   *   preference votes, so that empty ballots are not included.
   *   
   * @refernce http://www.cev.ie/htm/tenders/pdf/1_2.pdf, section 3, page 12 
   * @return The candidate ID of the first preference for this ballot
   */
  /*@ public normal_behavior
    @  requires 0 < numberOfPreferences;
    @  ensures \result != NONTRANSFERABLE;
    @  ensures \result == preferenceList[0];
    @*/
  public /*@ pure @*/ long getFirstPreference();
  
  /**
   * Load the ballot details
   * 
   * @param candidateIDList List of candidate IDs in order from first
   *   preference
   * 
   * @param listSize Number of candidate IDs in the list
   * 
   * @param uniqueID The serial number of the ballot or equivalent
   * 
   * @design There should be at least one preference in the list.
   *   Empty or spoilt votes should neither be loaded nor counted.
   *   There should be no duplicate preferences in the list and none
   *   of the candidate ID values should match the special value for
   *   non transferable votes.
   *   <p> There should be no duplicates in the preference list; but
   *   there is no need to make this a precondition because duplicates
   *   will be ignored and skipped over.
   */
  /*@ public normal_behavior
    @   requires 0 <= listSize;
    @   requires (\forall int i; 0 <= i && i < listSize;
    @     (candidateIDList[i]) != NONTRANSFERABLE);
    @   ensures numberOfPreferences == listSize;
    @   ensures ballotID == uniqueID;
    @   ensures (\forall int i; 0 <= i && i < listSize;
    @     (preferenceList[i] == candidateIDList[i]));
    @*/
  public void load(long[] candidateIDList, int listSize, long uniqueID);
  
  /**
   * Get candidate ID to which this ballot is assigned
   * 
   * @return The candidate ID to which this ballot is assigned
   */
  /*@ public normal_behavior 
    @   requires 0 <= positionInList;
    @   requires positionInList <= numberOfPreferences;
    @   requires preferenceList != null;
    @   ensures (positionInList == numberOfPreferences) ==> 
    @     (\result == NONTRANSFERABLE);
    @   ensures (positionInList < numberOfPreferences) ==>
    @     (\result == preferenceList[positionInList]);
    @*/
  public /*@ pure @*/ long getCandidateID();
  
  /**
   * Get next preference candidate ID
   * 
   * @param offset The number of preferences to look ahead
   *  
   * @return The next preference candidate ID
   */
  /*@ public normal_behavior 
    @   requires 0 <= positionInList;
    @   requires 1 <= offset;
    @   requires positionInList <= numberOfPreferences;
    @   requires preferenceList != null;
    @   ensures (positionInList + offset >= numberOfPreferences) ==> 
    @     (\result == NONTRANSFERABLE);
    @   ensures (positionInList + offset < numberOfPreferences) ==>
    @     (\result == preferenceList[positionInList + offset]);
    @*/
  public /*@ pure @*/ long getNextPreference(int offset);
  
  /**
   * Transfer this ballot to the next preference candidate
   * 
   * @design This method may be called multiple times during the same
   *   count until the ballot is nontransferable or a continuing
   *   candidate ID is found in the remainder of the preference list.
   * 
   * @param countNumber The count number at which the ballot was
   *   transfered
   */
  /*@ public normal_behavior
    @   requires 0 <= positionInList;
    @   requires positionInList <= numberOfPreferences;
    @   requires countNumberAtLastTransfer <= countNumber;
    @   assignable countNumberAtLastTransfer, positionInList;
    @   ensures countNumberAtLastTransfer == countNumber;
    @   ensures \old(positionInList) <= positionInList;
    @   ensures (positionInList == \old(positionInList) + 1) ||
    @     (positionInList == numberOfPreferences); 
    @*/
  public void transfer(long countNumber);
  
  /**
   * Get ballot ID number.
   * 
   * @return ID number for this ballot
   */
  /*@ public normal_behavior
    @   ensures \result == ballotID;
    @*/
  public /*@ pure @*/ long getBallotID();
  
  /**
   * This method checks if this ballot paper is assigned to this candidate.
   * 
   * @design It is valid to use <code>NONTRANSFERABLE</code> as the ID value to
   * be checked.  This ballot paper can only be assigned to one candidate at a time;
   * there is no concept of fractional transfers of votes in the Irish electoral
   * system.
   * 
   * @param candidateIDToCheck The unique identifier for this candidate.
   * 
   * @return <code>true</code> if this ballot paper is assigned to this candidate ID
   */
  /*@ public normal_behavior
    @   requires (0 < candidateIDToCheck) || 
    @     (candidateIDToCheck == NONTRANSFERABLE);
    @   ensures (\result == true) <==> (candidateID == candidateIDToCheck); 
    @*/
  public /*@ pure @*/ boolean isAssignedTo (long candidateIDToCheck);
  
  /**
   * Gets remaining number of preferences.
   * 
   * @return The number of preferences remaining
   */
  /*@
    @ public normal_behavior
    @   requires positionInList <= numberOfPreferences;
    @   ensures \result == numberOfPreferences - positionInList;
    @*/
  public /*@ pure @*/ long remainingPreferences();
  
  /**
   * Compares with another ballot paper's secret random number.
   * 
   * @design It is intended to be able to compare random numbers without
   * revealing the exact value of the random number, so that the random
   * number cannot be manipulated in any way.
   * 
   * @param other
   *   Other ballot to compare with this ballot
   *   
   * @return <code>true</code> if other ballot has lower random number
   */
  /*@ public normal_behavior
    @   requires this.randomNumber != other.randomNumber;
    @   ensures (\result == true) <==> (this.randomNumber > other.randomNumber);
    @*/
  public /*@ pure @*/ boolean isAfter (Ballot other);
}
