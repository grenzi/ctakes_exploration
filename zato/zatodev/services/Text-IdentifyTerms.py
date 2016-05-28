from zato.server.service import Service

class IdentifyTerms(Service):
    class SimpleIO:
        input_required = ('text',)
        output_required = ('terms', 'cid')

    def handle(self):
        self.logger.info('Request: {}'.format(self.request.payload))
        self.logger.info('Request type: {}'.format(type(self.request.payload)))


        out = self.outgoing.plain_http.get('ctakes')
        
        url_params = {}
        url_params['text'] = self.request.input.text

        response = out.conn.get(self.cid, url_params)

        self.response.payload.terms = response.text
        self.response.payload.cid = self.cid

        self.logger.info(response.text)

    @staticmethod
    def get_name():
        return 'text-identifyterms'

'''
{"text":"Present Illness:\r\nThe patient is status post two weeks from a left shoulder arthroscopy with capsular release and manipulation under anesthesia.  Overall she has done well postoperatively.  She presents today with no complications.  She did have an allergic reaction to the prep that we did preoperatively in the operating room.  She sustained a mild rash, but it is resolved since taking Benadryl and using hydrocortisone cream.  There are no pustules or redness, and she has well healing portal sites on her left shoulder.  \r\nPast Medical History:\r\nThe patient\u2019s past medical history was reviewed, updated, and filed in the Medical History tab in the chart. \r\nExamination:\r\nOn physical exam, the patient is alert and oriented x 3.  She is here today with her husband.  Her sutures were removed.  She has well healing portal sites on her left shoulder.  There is no sign of erythema, drainage, or infection noted postoperatively.  She has good range of motion.  She has about 90o of forward elevation on the left shoulder.  She can externally rotate to approximately 15o, and she can internally rotate to 15o on her left shoulder.  \r\nDiagnosis:\r\nStatus post left shoulder adhesive capsulitis and subacromial bursitis two weeks status post left shoulder arthroscopy and manipulation under anesthesia. "} 
'''